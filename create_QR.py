import qrcode

def create_QR(id_student):
	qr = qrcode.QRCode(version=1, box_size=10, border=5)
	qr.add_data(id_student)
	qr.make(fit=True)
	img = qr.make_image(fill='black', back_color='white')
	link_qr = 'static/'+id_student+'.jpg'
	img.save(link_qr)
	return link_qr
