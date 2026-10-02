import pandas as pd

try:
    # Intentamos cargar un archivo para probar
    df_sales = pd.read_csv('ecommerce_sales_customer.csv')
    print("¡Perfecto! Python funciona y encontró tu base de datos.")
    print("Columnas detectadas:", list(df_sales.columns))
except Exception as e:
    print("Error al leer el archivo. Revisa que el nombre esté idéntico:", e)