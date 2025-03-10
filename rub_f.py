################# Función para cargar los archivos en DataFrame #################################################################

#Esta función leerá como si fuese una "cadena" el nombre del archivo y determinará la lectura correcta para pasarlo a Data Frame
def cargar_dataset (archivo):
    import pandas as pd
    import os

    extension = os.path.splitext(archivo)[1].lower()  #dividimoa el nombre del archivo y extraemos la extensión

    #Y ahora soo hacemos una comparativa para determinar el tipo de archivo que tenemos
    if extension == '.csv': 
        return pd.read_csv(archivo)    #Y de acuerdo al tipo de archivo lo convertimos a Data Frame

    elif extension == '.xlsx':
        return pd.read_excel(archivo)

    elif extension == '.json':
        return pd.read_json(archivo)
    
    elif extension == '.html':
        return pd.read_html(archivo)
    
    else:
        raise ValueError(f'Formato de archivo no soportado: {extension}')
    

################### Conteo de valores nulos ###########################################################################

def val_nu(dataframe): #Tomamos como parámetro el Data Frame que se analizara
    valo_nu_col = dataframe.isnull().sum()  #Y solo hacemos la suma de nulos detectados en el DataFrame
    valo_nu_tot = dataframe.isnull().sum().sum()

    return('Valores nulos por columna:',valo_nu_col,
           "Valores nulos en total:", valo_nu_tot)   #Y los imprimimos

################### Sustitución de valores nulos por metodo ffill y por mediana #####################################################

def vn_ff(dataframe):
    import pandas as pd
    #Vamos a separar columnas cuantitativas del data frame
    col_cuan = dataframe.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    #Ahora separamos las columnas con datos cualitativas
    col_cual = dataframe.select_dtypes(include=['object', 'datetime', 'category'])
    #Sustituimos las variables cualitativas mediante el método ffill y las cuantitativas por la mediana (aclaro uso dos métodos en todas las funciones para tener mejores resuñtados)
    cual = col_cual.fillna(method='ffill')
    cuan = col_cuan.fillna(round(col_cuan.median(), 1))
    #Unimos el data frame
    dt_f = pd.concat([cuan,cual], axis=1)
    return(dt_f)

################### Sustitución de valores nulos por metodo bfill y por promedio #####################################################

def vn_bf(dataframe):
    import pandas as pd
    #Vamos a separar columnas cuantitativas del data frame
    col_cuan = dataframe.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    #Ahora separamos las columnas con datos cualitativas
    col_cual = dataframe.select_dtypes(include=['object', 'datetime', 'category'])
    #Sustituimos las variables cualitativas mediante el método bfill y las cuantitativas por el promedio
    cual = col_cual.fillna(method='bfill')
    cuan = col_cuan.fillna(round(col_cuan.mean(), 1))
    #Unimos el data frame
    dt_f = pd.concat([cuan,cual], axis=1)
    return(dt_f)

################### Sustitución de valores nulos por un string conctreto y por promedio #####################################################

def rempl_vn_str(dataframe):
    import pandas as pd
    #Vamos a separar columnas cuantitativas del data frame
    col_cuan = dataframe.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    #Ahora separamos las columnas con datos cualitativas
    col_cual = dataframe.select_dtypes(include=['object', 'datetime', 'category'])
    #Sustituimos las variables cualitativas por un string concreto y las cuantitativas por promedio
    cual = col_cual.fillna(" ")
    cuan = col_cuan.fillna(round(col_cuan.mean(), 1))
    #Unimos el data frame
    dt_f = pd.concat([cuan,cual], axis=1)
    return(dt_f)

################### Sustitución de valores nulos por promedio y metódo bfill ################################################################################
def vn_promedio(dataframe):
    import pandas as pd
    #Vamos a separar columnas cuantitativas del data frame
    col_cuan = dataframe.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    #Ahora separamos las columnas con datos cualitativas
    col_cual = dataframe.select_dtypes(include=['object', 'datetime', 'category'])
    #Sustituimos las variables cualitativas mediante el método bfill y las cuantitativas por el promedio
    cual = col_cual.fillna(method='bfill')
    cuan = col_cuan.fillna(round(col_cuan.mean(), 1))
    #Unimos el data frame
    dt_f = pd.concat([cuan, cual], axis=1)
    return(dt_f)

################### Sustitución de valores nulos por mediiana y metódo ffill ################################################################################
def vn_promedio(dataframe):
    import pandas as pd
    #Vamos a separar columnas cuantitativas del data frame
    col_cuan = dataframe.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    #Ahora separamos las columnas con datos cualitativas
    col_cual = dataframe.select_dtypes(include=['object', 'datetime', 'category'])
    #Sustituimos las variables cualitativas mediante el método ffill y las cuantitativas por la mediana
    cual = col_cual.fillna(method='ffill')
    cuan = col_cuan.fillna(round(col_cuan.median(), 1))
    #Unimos el data frame
    dt_f = pd.concat([cuan, cual], axis=1)
    return(dt_f)

################### Sustitución de valores nulos por una constante y metódo ffill ################################################################################
def vn_constante(dataframe):
    import pandas as pd
    #Vamos a separar columnas cuantitativas del data frame
    col_cuan = dataframe.select_dtypes(include=['float64', 'int64', 'float', 'int'])
    #Ahora separamos las columnas con datos cualitativas
    col_cual = dataframe.select_dtypes(include=['object', 'datetime', 'category'])
    #Sustituimos las variables cualitativas mediante el método bfill y las cuantitativas por una constante especifica
    cual = col_cual.fillna(method='bfill')
    cuan = col_cuan.fillna(25)
    #Unimos el data frame
    dt_f = pd.concat([cuan, cual], axis=1)
    return(dt_f)
