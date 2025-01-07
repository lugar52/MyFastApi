class Querys_perneria:

    #Sentencias a la base de datos
    
    QUERY_ALL_PERNERIA = "SELECT ID_PERNO, OC, CONTRATO, GUIA, SNF, BULTO, ITEMCODE, TIPO_ELEMENTO, MARCA, MARCA2, TUNEL, DISPOSICION_FINAL, CANTIDAD_SNF, \
                        CANTIDAD_TERRENO, DIFERENCIA, PESO_UNITARIO, PESO_TOTAL, PROVEEDOR, PATIO, FECHA_LLEGADA, OBSERVACION, NB_ASIG_TERR \
                        FROM railway.control_perneria;"
    
    QUERY_PERNERIA_X_SNF = "SELECT P.ID_PERNO, P.OC, P.CONTRATO, P.GUIA, P.SNF, P.BULTO, P.ITEMCODE, P.TIPO_ELEMENTO, P.MARCA, P.MARCA2, P.TUNEL, \
    P.DISPOSICION_FINAL, P.CANTIDAD_SNF, P.CANTIDAD_TERRENO, P.DIFERENCIA, P.PESO_UNITARIO, P.PESO_TOTAL, P.PROVEEDOR, P.PATIO, P.FECHA_LLEGADA,  \
    P.OBSERVACION, P.NB_ASIG_TERR, TP.ID_TPELEMENTO,  TU.ID_TUNEL,  DI.ID_DISP_FINAL, PR.ID_PROVEEDOR, PA.ID_PATIO \
    FROM control_perneria P \
    INNER JOIN TIPO_ELEMENTO TP \
        ON P.TIPO_ELEMENTO = TP.ID_TPELEMENTO \
    INNER JOIN TUNEL TU \
        ON P.TUNEL = TU.ID_TUNEL \
    INNER JOIN disposicion DI \
        ON P.DISPOSICION_FINAL = DI.ID_DISP_FINAL  \
    INNER JOIN proveedor PR \
        ON P.PROVEEDOR = PR.ID_PROVEEDOR  \
    INNER JOIN PATIO PA \
        ON P.PATIO = PA.ID_PATIO \
    "
    
    QUERY_PERNERIA_PENDIENTES = "SELECT ID_PERNO, OC, CONTRATO, GUIA, SNF, BULTO, ITEMCODE, TIPO_ELEMENTO, MARCA, MARCA2, TUNEL, DISPOSICION_FINAL, CANTIDAD_SNF, \
    CANTIDAD_TERRENO, DIFERENCIA, PESO_UNITARIO, PESO_TOTAL, PROVEEDOR, PATIO, FECHA_LLEGADA, OBSERVACION, NB_ASIG_TERR \
    FROM railway.control_perneria  WHERE DIFERENCIA != 0"

    QUERY_PERNERIA_COMPLETAS = "SELECT ID_PERNO, OC, CONTRATO, GUIA, SNF, BULTO, ITEMCODE, TIPO_ELEMENTO, MARCA, MARCA2, TUNEL, DISPOSICION_FINAL, CANTIDAD_SNF, \
    CANTIDAD_TERRENO, DIFERENCIA, PESO_UNITARIO, PESO_TOTAL, PROVEEDOR, PATIO, FECHA_LLEGADA, OBSERVACION, NB_ASIG_TERR \
    FROM railway.control_perneria  WHERE DIFERENCIA = 0"
