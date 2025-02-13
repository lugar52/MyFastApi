class Querys_perneria:

    #Sentencias a la base de datos
        
    QUERY_PERNERIA = "SELECT P.ID_PERNO, P.OC, P.CONTRATO, P.GUIA, P.SNF, P.BULTO, P.ITEMCODE, P.TIPO_ELEMENTO, P.MARCA, ifnull(P.TUNEL , 0) as TUNEL, \
    P.DISPOSICION_FINAL, P.CANTIDAD_SNF, P.CANTIDAD_TERRENO, P.DIFERENCIA, P.PESO_UNITARIO, P.PESO_TOTAL, P.PROVEEDOR, P.PATIO, \
    STR_TO_DATE(P.FECHA_LLEGADA, '%d-%m-%Y') AS FECHA_LLEGADA,  \
    P.OBSERVACION, P.NB_ASIG_TERR, TP.DESCRIPCION as TIPOELEM_DESCRIPCION,  TU.DESCRIPCION as TUNEL_DESCRIPCION,  DI.DESCRIPCION as DISPO_DESCRIPCION, \
    PR.DESCRIPCION as PROVE_DESCRIPCION, PA.DESCRIPCION as PATIO_DESCRIPCION, \
    ROUND((CANTIDAD_TERRENO/CANTIDAD_SNF)*100, 2) AS PORCENTAJE, 0 as isEdit, false as isSelected, P.CANT_DESPACHOS , P.STOCK , \
    SP.Descripcion as SUBPATIO_DESCRIPCION, ifnull(SP.ID_SubPatio, 0) AS ID_SubPatio , C.Descripcion AS COORDENADA_DESCRIPCION, ifnull(C.ID_Coordenada, 0) AS ID_Coordenada, P.GUIA_PROVEEDOR, P.UNIDAD, P.CAJON_PALLET_JAVA, P.RECEPCIONADO, P.ELEMENTO, e.descripcion AS ELEMENTO_DESC  \
    FROM control_perneria P \
        LEFT JOIN TIPO_ELEMENTO TP ON P.TIPO_ELEMENTO = TP.ID_TPELEMENTO \
        LEFT JOIN TUNEL TU ON P.TUNEL = TU.ID_TUNEL \
        LEFT JOIN disposicion DI ON P.DISPOSICION_FINAL = DI.ID_DISP_FINAL  \
        LEFT JOIN proveedor PR ON P.PROVEEDOR = PR.ID_PROVEEDOR  \
        LEFT JOIN PATIO PA ON P.PATIO = PA.ID_PATIO \
        LEFT JOIN SubPatio SP ON P.SUB_PATIO = SP.ID_SubPatio \
        LEFT JOIN Coordenadas C on P.COORDENADAS = C.ID_Coordenada \
        LEFT JOIN elementos e on P.ELEMENTO = e.Id_elementos " 