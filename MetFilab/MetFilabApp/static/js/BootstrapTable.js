function drawDataTable(id, dataColumns, dataRows) {
	var tableId = "#" + id;

	$(tableId).bootstrapTable({
		height: 400,
		showColumns: true,
		columns: dataColumns,
		data: dataRows,
		pagination: true,
		pageList: [10,20,40,80,160,'All'],
	});

}