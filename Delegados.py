import streamlit as st

st.title("Elección de Delegados")

# Lista inicial de candidatos
candidatos = ["Amira", "Sabrina", "Dario", "Kata"]
votos = {c: 0 for c in candidatos}

# Postulación de nuevos candidatos
nombre = st.text_input("Tu nombre")
if st.button("Postularme"):
    if nombre and nombre not in candidatos:
        candidatos.append(nombre)
        votos[nombre] = 0
        st.success(f"{nombre} se postuló correctamente")
    elif nombre in candidatos:
        st.warning("Ese nombre ya está en la lista")

# Votación
candidato = st.selectbox("Selecciona un candidato", candidatos)
if st.button("Votar"):
    votos[candidato] += 1
    st.info(f"Votaste a {candidato}")

# Resultados
if st.button("Ver resultados"):
    st.subheader("Resultados actuales")
    for c in candidatos:
        st.write(f"{c}: {votos[c]} votos")
