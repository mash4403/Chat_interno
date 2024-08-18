import pandas as pd

print("Cargando datos desde Excel...")
file_path = '/Users/miguelangel/Documents/inteligencia artificial/REPOSITORIOS/Chat_interno/Data/data.xlsx'  # Asegúrate de que la ruta al archivo Excel es correcta
data = pd.read_excel(file_path)

print("Convirtiendo datos a JSON...")
json_data = data.to_json(orient='records', force_ascii=False)

output_path = '/Users/miguelangel/Documents/inteligencia artificial/REPOSITORIOS/Chat_interno/Data.json'
print("Guardando JSON en:", output_path)

try:
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(json_data)
    print("Archivo guardado exitosamente!")
except Exception as e:
    print("Error al guardar el archivo:", e)
