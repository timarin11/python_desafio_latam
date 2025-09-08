{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d2b3c04e-4eec-4f49-8d90-395940f3b7d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "contenido = \"\"\"import pandas as pd\n",
    "\n",
    "# ---------------------------\n",
    "# 1. Función para filtrar por fechas\n",
    "# ---------------------------\n",
    "def filtrar_por_fecha(df, columna_fecha, fecha_inicio, fecha_fin):\n",
    "    '''\n",
    "    Filtra un DataFrame entre un rango de fechas dado.\n",
    "    '''\n",
    "    df[columna_fecha] = pd.to_datetime(df[columna_fecha])\n",
    "    return df[(df[columna_fecha] >= fecha_inicio) & (df[columna_fecha] <= fecha_fin)]\n",
    "\n",
    "\n",
    "# ---------------------------\n",
    "# 2. Función para generar reportes (pivot_table)\n",
    "# ---------------------------\n",
    "def generar_reporte(df, filas_index, columnas=None, valores=None, medida=\"sum\"):\n",
    "    '''\n",
    "    Genera un reporte en formato de tabla pivote.\n",
    "    '''\n",
    "    return pd.pivot_table(\n",
    "        df,\n",
    "        index=filas_index,\n",
    "        columns=columnas,\n",
    "        values=valores,\n",
    "        aggfunc=medida,\n",
    "        fill_value=0\n",
    "    ).reset_index()\n",
    "\n",
    "\n",
    "# ---------------------------\n",
    "# 3. Función para guardar en PostgreSQL\n",
    "# ---------------------------\n",
    "def guardar_en_postgres(df, nombre_tabla, engine, if_exists=\"replace\"):\n",
    "    '''\n",
    "    Guarda un DataFrame en PostgreSQL.\n",
    "    '''\n",
    "    df.to_sql(nombre_tabla, engine, if_exists=if_exists, index=False)\n",
    "    print(f\"✅ Tabla '{nombre_tabla}' guardada en PostgreSQL con {len(df)} registros.\")\n",
    "\"\"\"\n",
    "\n",
    "# Sobrescribir archivo limpio\n",
    "with open(\"funciones.py\", \"w\", encoding=\"utf-8\") as f:\n",
    "    f.write(contenido)\n",
    "\n",
    "print(\"✅ Archivo funciones.py creado correctamente\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0960c603-bbc7-4c9f-9e0b-c66d4bde83ca",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
