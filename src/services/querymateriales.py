class Querys_materiales:

    #Sentencias a la base de datos  
    
    QUERY_MATERIALES = "SELECT M.ID_cmaterial, M.OC, M.PO, M.guia, M.snf, M.marca, M.cantidad_snf, M.cantidad_terreno, M.diferencia, \
	M.id_elemento, e.descripcion ,  \
	M.id_disposicion, DI.DESCRIPCION, \
	M.id_tipo_elem, TP.DESCRIPCION, \
	M.peso_unitario, M.peso_total, M.bulto,  \
	M.id_proveedor, PR.descripcion, \
	M.id_patio_1, SP.Descripcion , \
	M.id_coordenada, C.Descripcion , \
	M.id_patio, PA.descripcion, \
	STR_TO_DATE(M.fecha_llegada, '%d-%m-%Y') AS FECHA_LLEGADA,  \
	M.observacion, \
    ROUND((CANTIDAD_TERRENO/CANTIDAD_SNF)*100, 2) AS PORCENTAJE, 0 as isEdit, false as isSelected \
	FROM railway.control_materiales M \
		INNER JOIN elementos e ON M.id_elemento = e.Id_elementos \
		INNER JOIN disposicion DI ON M.id_disposicion = DI.ID_DISP_FINAL \
		INNER JOIN TIPO_ELEMENTO TP ON M.id_tipo_elem = TP.ID_TPELEMENTO \
		INNER JOIN proveedor PR ON M.id_proveedor = PR.ID_PROVEEDOR \
    	INNER JOIN PATIO PA ON M.id_patio = PA.ID_PATIO \
    	INNER JOIN SubPatio SP ON M.id_patio_1 = SP.ID_SubPatio \
    	INNER JOIN Coordenadas C on M.id_coordenada = C.ID_Coordenada \
    "
    
    