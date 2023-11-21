import requests
from reportlab.pdfgen import canvas
from io import BytesIO
from PIL import Image

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        return None

def save_images_to_pdf(base_url, start_index, end_index, output_pdf):
    pdf_buffer = BytesIO()
    pdf = canvas.Canvas(pdf_buffer)

    for idx in range(start_index, end_index + 1):
        url = f"{base_url}/{idx}"
        image_data = download_image(url)
        if image_data:
            # Simpan gambar ke file sementara
            temp_filename = f"temp_image_{idx}.png"
            with open(temp_filename, 'wb') as temp_file:
                temp_file.write(image_data.getvalue())

            # Baca kembali gambar sebagai Image
            image = Image.open(temp_filename)
            width, height = image.size

            # Gambar ke PDF
            pdf.setPageSize((width, height))
            pdf.drawInlineImage(temp_filename, 0, 0, width, height)
            if idx < end_index:
                pdf.showPage()

            # Hapus file sementara
            os.remove(temp_filename)

    pdf.save()

    with open(output_pdf, 'wb') as pdf_file:
        pdf_file.write(pdf_buffer.getvalue())

if __name__ == "__main__":
    import os

    base_url = "LINK" # Gantilah dengan URL yang sesuai
    start_index = 0
    end_index = 60  # Gantilah dengan indeks terakhir gambar yang ingin Anda unduh
    output_pdf_file = "NAMA-OUTPUT.pdf" # Gantilah dengan nama file PDF yang ingin Anda buat

    save_images_to_pdf(base_url, start_index, end_index, output_pdf_file)
    print(f"PDF berhasil dibuat: {output_pdf_file}")
