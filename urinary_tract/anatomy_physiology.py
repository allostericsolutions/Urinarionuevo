import streamlit as st

# Variable para controlar la visibilidad de la sección de anatomía y fisiología
mostrar_anatomia = False

# Botón para mostrar la sección de anatomía y fisiología
if st.button("Show Anatomy and Physiology"):
    mostrar_anatomia = not mostrar_anatomia

# Sección que se expande y se contrae para anatomía y fisiología
with st.expander("Anatomy and Physiology of the Kidney - Flash Card Style:", expanded=mostrar_anatomia):
    st.write("**1. Urinary System Components**")
    st.write("    - Upper urinary tract: kidneys and ureters")
    st.write("    - Lower urinary tract: bladder and urethra")
    st.write("**2. Functional Unit: Nephron**")
    st.write("**3. Nephron Development**")
    st.write("    - Functions by the 9th week of gestation")
    st.write("    - Urine production starts between 11-13 weeks")
    st.write("**4. Importance for Fetus: Urine forms the majority of amniotic fluid**")
    st.write("**5. Kidneys' Functions**")
    st.write("    - Detoxify and filter blood")
    st.write("    - Excrete metabolic waste")
    st.write("    - Reabsorb amino acids, ions, glucose, and water")
    st.write("    - Maintain pH, iron, and salt balance")
    st.write("    - Regulate blood pressure via renin")
    st.write("**6. Embryonic Development**")
    st.write("    - Formed by 2 parenchymal masses (renunculi or ranunculi)")
    st.write("    - Initially in the pelvis, ascend to abdomen by 12 weeks")
    st.write("**7. Ectopic Kidney**")
    st.write("    - Most common location: pelvis")
    st.write("    - Ascension can be arrested along the typical migratory path")
    st.write("**8. Adult Kidney Anatomy**")
    st.write("    - Bean-shaped, retroperitoneal")
    st.write("    - Left kidney higher due to liver size")
    st.write("    - Left kidney often slightly longer")
    st.write("**9. Kidney Coverings (from outside to inside)**")
    st.write("    - Pararenal fat layer")
    st.write("    - Gerota fascia")
    st.write("    - Perirenal fat layer")
    st.write("    - Renal capsule")
    st.write("**10. Kidney Parts**")
    st.write("    - Renal parenchyma: includes renal medulla (absorption, renal pyramids) and renal cortex (blood filtration)")
    st.write("    - Renal sinus: contains the renal collecting system (minor calices, major calices, renal pelvis, and infundibula)")
    st.write("**11. Renal Pelvis: Funnel-shaped, collects urine before moving to the ureter**")
    st.write("**Vascular Anatomy of the Kidneys**")
    st.write("**12. Renal Arteries**")
    st.write("    - Branch from abdominal aorta below superior mesenteric artery")
    st.write("    - Enter renal hilum, then segmental branches, interlobar arteries")
    st.write("    - Interlobar arteries → arcuate arteries → interlobular arteries → afferent arterioles")
    st.write("**13. Afferent Arterioles: Carry blood to the glomerulus for filtration**")
    st.write("**14. Right Renal Artery: Longer, travels posterior to the inferior vena cava (IVC)**")
    st.write("**15. Renal Veins**")
    st.write("    - Exit at renal hilum, connect to the IVC")
    st.write("    - Left renal vein: crosses between superior mesenteric artery and abdominal aorta, longer than right")
    st.write("**16. Left Renal Vein Diameter**")
    st.write("    - Smaller as it travels between the superior mesenteric artery and abdominal aorta")
    st.write("    - More prominent past this point towards the kidney")
