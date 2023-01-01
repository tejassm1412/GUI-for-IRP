from fpdf import FPDF

def pdf_create(name, email, mNo, orgo, pov):
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 10)

    data={'name': name,'Email Address':email, 'Mobile Number': mNo, 'Organization': orgo, 'POV': pov}
    
    pdf.cell(200,10,f"Name:  {data['name']}",ln=1,align='L')
    pdf.cell(200,10,f"Email: {data['Email Address']}",ln=2,align='L')
    pdf.cell(200,10,f"Mobile No.: {data['Mobile Number']}",ln=3,align='L')
    pdf.cell(200,10,f"Organization: {data['Organization']}",ln=4,align='L')
    pdf.cell(200,10,f"Purpose of Visit: {data['POV']}",ln=5,align='L')
    pdf.image(f'/home/tejas/Desktop/My STuff/27-10-2022/Progress/img.jpg',x=10,y=60,w=60,h=70)
    pdf.output(f"/home/tejas/Desktop/My STuff/27-10-2022/Progress/PDFs/{data['name']}_LTTS_Pass.pdf")