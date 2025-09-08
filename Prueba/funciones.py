import pandas as pd


# 1. Función para filtrar por fechas. Sirve para realizar reportes en dentro de ciertas franjas temporales

def filtrar_por_fecha(df, columna_fecha, fecha_inicio, fecha_fin):
    """
    Filtra un DataFrame entre un rango de fechas dado.
    """
    df[columna_fecha] = pd.to_datetime(df[columna_fecha]) # Convertir a datetime el objeto
    return df[(df[columna_fecha] >= fecha_inicio) & (df[columna_fecha] <= fecha_fin)] # Filtra valores mayores o igual a fecha inicio y menor o igual a fecha final



# 2. Función para generar reportes como tablas pivote con a partir de un data frame con informacion de ventas. Por default calcula totales

def generar_reporte(df, filas_index, columnas=None, valores=None, medida="sum"):
    """
    Genera un reporte en formato de tabla pivote.
    """
    return pd.pivot_table(
        df,
        index=filas_index, # Valores a partir de los cuales se quiere agrupar
        columns=columnas, 
        values=valores, # valores que se quieren calcular
        aggfunc=medida, # default de medida = suma
        fill_value=0
    ).reset_index()



# 3. Función para guardar en PostgreSQL. Se utiliza para guardar reporte como una nueva tabla en SQL

def guardar_en_postgres(df, nombre_tabla, engine, if_exists="replace"):
    """
    Guarda un DataFrame en PostgreSQL.
    """
    df.to_sql(nombre_tabla, engine, if_exists=if_exists, index=False)
    print(f"✅ Tabla '{nombre_tabla}' guardada en PostgreSQL con {len(df)} registros.")
