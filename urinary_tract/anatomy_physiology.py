import streamlit as st

# Variable para controlar la visibilidad de la sección de anatomía y fisiología
mostrar_anatomia = False

# Botón para mostrar la sección de anatomía y fisiología
if st.button("Show Anatomy and Physiology"):
    mostrar_anatomia = not mostrar_anatomia

# Función para estilizar los títulos
def style_title(title):
    return f"<span style='color:darkorange; font-weight:bold;'>{title}</span>"

# Sección que se expande y se contrae para anatomía y fisiología
with st.expander("Anatomy and Physiology of the Kidney - Flash Card Style:", expanded=mostrar_anatomia):
    st.markdown(style_title("1. Urinary System Components"), unsafe_allow_html=True)
    st.write("    - Upper urinary tract: kidneys and ureters")
    st.write("    - Lower urinary tract: bladder and urethra")

    st.markdown(style_title("2. Functional Unit"), unsafe_allow_html=True)
    st.write("    - Nephron")
    
    st.markdown(style_title("3. Nephron Development"), unsafe_allow_html=True)
    st.write("    - Functions by the 9th week of gestation")
    st.write("    - Urine production starts between 11-13 weeks")
   
    st.markdown(style_title("4. Importance for Fetus"), unsafe_allow_html=True)
    st.write("    - Urine forms the majority of amniotic fluid")
   
    st.markdown(style_title("5. Kidneys' Functions"), unsafe_allow_html=True)
    st.write("    - Detoxify and filter blood")
    st.write("    - Excrete metabolic waste")
    st.write("    - Reabsorb amino acids, ions, glucose, and water")
    st.write("    - Maintain pH, iron, and salt balance")
    st.write("    - Regulate blood pressure via renin")
   
    st.markdown(style_title("6. Embryonic Development"), unsafe_allow_html=True)
    st.write("    - Formed by 2 parenchymal masses (renunculi or ranunculi)")
    st.write("    - Initially in the pelvis, ascend to abdomen by 12 weeks")
   
    st.markdown(style_title("7. Ectopic Kidney"), unsafe_allow_html=True)
    st.write("    - Most common location: pelvis")
    st.write("    - Ascension can be arrested along the typical migratory path")
   
    st.markdown(style_title("8. Adult Kidney Anatomy"), unsafe_allow_html=True)
    st.write("    - Bean-shaped, retroperitoneal")
    st.write("    - Left kidney higher due to liver size")
    st.write("    - Left kidney often slightly longer")
   
    st.markdown(style_title("9. Kidney Coverings (from outside to inside)"), unsafe_allow_html=True)
    st.write("    - Pararenal fat layer")
    st.write("    - Gerota fascia")
    st.write("    - Perirenal fat layer")
    st.write("    - Renal capsule")
   
    st.markdown(style_title("10. Kidney Parts"), unsafe_allow_html=True)
    st.write("    - Renal parenchyma: includes renal medulla (absorption, renal pyramids) and renal cortex (blood filtration)")
    st.write("    - Renal sinus: contains the renal collecting system (minor calices, major calices, renal pelvis, and infundibula)")
   
    st.markdown(style_title("11. Renal Pelvis"), unsafe_allow_html=True)
    st.write("    - Funnel-shaped, collects urine before moving to the ureter")
    
    st.markdown(style_title("12. Vascular Anatomy of the Kidneys"), unsafe_allow_html=True)
    st.write("    - Renal Arteries")
    st.write("        - Branch from abdominal aorta below superior mesenteric artery")
    st.write("        - Enter renal hilum, then segmental branches, interlobar arteries")
    st.write("        - Interlobar arteries → arcuate arteries → interlobular arteries → afferent arterioles")
    st.write("    - Afferent Arterioles")
    st.write("        - Carry blood to the glomerulus for filtration")
    st.write("    - Right Renal Artery")
    st.write("        - Longer, travels posterior to the inferior vena cava (IVC)")
    st.write("    - Renal Veins")
    st.write("        - Exit at renal hilum, connect to the IVC")
    st.write("        - Left renal vein: crosses between superior mesenteric artery and abdominal aorta, longer than right")
        
    st.markdown(style_title("13. Left Renal Vein Diameter"), unsafe_allow_html=True)
    st.write("    - Smaller as it travels between the superior mesenteric artery and abdominal aorta")
    st.write("    - More prominent past this point towards the kidney")
