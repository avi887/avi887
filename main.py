# This is a sample Python script.
import PIL
from PIL import Image
image = Image.open('IMAGE777.jpg')
image=image.resize((600,400))
import streamlit as st
st.title("HAPPY NEW YEAR TOKTOK")
option = st.selectbox(
    'CHOOSE YOUR BESTFRIENDS NAME OF 2022',
    ('AVTAR SAHANI','AVI','MONA MAAM','AFRIN','ANTHONY'))
image2= Image.open('image2.jpg')
image3=Image.open('image 3.jpg')
def bestfrnd():
    if option=='AVTAR SAHANI':
        st.write('Toktok yeah naam tum gusse se lete ho samje motu')
    elif option=='AVI':
        st.write('sahi jawab yahi tumhara bestfrnd hain')
    elif option=='ANTHONY':
        st.image(image)
    elif option=='AFRIN':
        st.image(image2,caption='CANCEL SPACE Y KO CHUNA HAIN AAPNE')
    elif option=='MONA MAAM':
        st.image(image3)
bestfrnd()
LIST1=['1: ENJOY YOUR EACH AND EVERY TIME']
LIST2=['2: GUSSA KAAM KARNA HAIN THODA']
LIST3=['3: NEW YEAR ME THODA APNE AAP KO TIME DENA HAIN']
LIST4=['4: GUMNA FIRNA HAIN JADA']
LIST5=['5: APNE AAP KO NEGATIVE LOGO SE DUR RAKHNA HAIN']
LIST6=['6: FIRST PRIORITY APNE AAP KO DENA HAIN TUMHE']
LIST7=['7: THODA MOTA HONA HAIN HAHAHA, PATLE HO TUM SACHII']
LIST8=['8: STORE SE NIKALNE K BAAD STORE KO DEMAK SE NIKALNA HAIN']
LIST9=['9: AVI AGAR GALTI KARE TOH USSE MAAF KARNA HAIN']
LIST10=['10: PERSONAL AUR PROFESSIONAL LIFE MIX NHI KARNA HAIN']
LIST11=['11: NEW FRNDS BANANE HAIN TUMHE']
LIST12=['12:FAMILY K SATH THODA JADA TIME SPEND KARNA HAIN TUMHE']
LIST13=['13: SAAL ME DO BAAR CHUTTI LEKE KAHI ADVENTURE PE JANA HAIN']
LIST14=['14: CAMPING KARNA HAIN']
LIST15=['15: GYM JANA HAIN PAR YEH OPTIONAL HAIN Q KI TUM WAISE HI FIT HO']
LIST16=['16: AUR BHI HAIN PAR WO BAAD ME BATAUNGA']
LIST17=['17: SORRY MAAF KARNA TOKTOK SATANE K LIYE ITNA YEH SAAL']
if st.button("Click here to see the new year list"):
     st.write(LIST1,LIST2,LIST3,LIST4,LIST5,LIST6,LIST7,LIST8,LIST9,LIST10,LIST11,LIST12,LIST13,LIST14,LIST15,LIST16,LIST17)
else:
    pass