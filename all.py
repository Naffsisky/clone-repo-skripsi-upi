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

def save_images_to_pdf(base_urls, start_index, end_index, output_pdf):
    pdf_buffer = BytesIO()
    pdf = canvas.Canvas(pdf_buffer)

    for base_url in base_urls:
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

    base_urls_set_1 = ["http://reader-repository.upi.edu/index.php/display/img/105033/1"]
    base_urls_set_2 = ["http://reader-repository.upi.edu/index.php/display/img/105033/2"]
    base_urls_set_3 = ["http://reader-repository.upi.edu/index.php/display/img/105033/3"]
    base_urls_set_4 = ["http://reader-repository.upi.edu/index.php/display/img/105033/4"]
    base_urls_set_5 = ["http://reader-repository.upi.edu/index.php/display/img/105033/5"]
    base_urls_set_6 = ["http://reader-repository.upi.edu/index.php/display/img/105033/6"]
    base_urls_set_7 = ["http://reader-repository.upi.edu/index.php/display/img/105033/7"]
    base_urls_set_8 = ["http://reader-repository.upi.edu/index.php/display/img/105033/8"]
    base_urls_set_9 = ["http://reader-repository.upi.edu/index.php/display/img/105033/9"]
    base_urls_set_10 = ["http://reader-repository.upi.edu/index.php/display/img/105033/10"]
    start_index = 1
    end_index = 60  # Gantilah dengan indeks terakhir gambar yang ingin Anda unduh
    output_pdf_file = "tes.pdf"

    base_urls = base_urls_set_1 + base_urls_set_2  + base_urls_set_3 + base_urls_set_4 + base_urls_set_5 + base_urls_set_6 + base_urls_set_7 + base_urls_set_8 + base_urls_set_9 + base_urls_set_10

    save_images_to_pdf(base_urls, start_index, end_index, output_pdf_file)
    print(f"PDF berhasil dibuat: {output_pdf_file}")
