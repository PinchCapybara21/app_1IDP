# 📊 Proyecto 1: Visualización de variables macro del país

---

## 📌 Fuentes de datos
- *Banco de la República* (series oficiales descargadas desde el portal estadístico).

---

## 📅 Periodo de análisis
- *2010 – 2024*

---

## ⏱ Frecuencia de las variables
- *PIB*: anual  
- *Desempleo*: anual (transformado desde datos mensuales)  
- *Inflación*: anual  

---

## 🔄 Transformaciones realizadas
- Descarga de las series oficiales del Banco de la República (2001–2024).  
- Limpieza de la base de datos para trabajar únicamente con *2010–2024*.  
- Renombramiento de columnas y cambio de tipos de datos de object a float.  
- Conversión del *desempleo de mensual a anual*.  
- Creación de la variable *ANIO* para realizar el merge entre las bases.  

---

## 📝 Supuestos
- No se realizaron supuestos adicionales en la construcción de las variables.
