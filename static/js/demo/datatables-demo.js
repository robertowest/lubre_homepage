// Call the dataTables jQuery plugin

$(document).ready(function() {
  $('#dataTable').DataTable({
    "language": {
      "decimal":        "",
      "emptyTable":     "No hay datos disponibles en la tabla",
      "info":           "Mostrando _START_ a _END_ de _TOTAL_ registros",
      "infoEmpty":      "No hay registros disponibles",
      "infoFiltered":   "(filtrado de _MAX_ registros)",
      "infoPostFix":    "",
      "thousands":      ",",
      "lengthMenu":     "Mostrar _MENU_ registros",
      "loadingRecords": "Cargando ...",
      "processing":     "Procesando ...",
      "search":         "Buscar:",
      "zeroRecords":    "No se encontraron registros",
      "paginate": {
          "first":      "Primero",
          "last":       "Último",
          "next":       "Siguiente",
          "previous":   "Anterior"
      },
      "aria": {
          "sortAscending":  ": activar para ordenar la columna ascendente",
          "sortDescending": ": activar para ordenar la columna descendente"
      }
    },
    "lengthMenu": [ 10, 15, 20, 50, 100 ],
    "ordering": false,
    "pageLength": 15,
    "recordsTotal": 100,
    "recordsFiltered": 100,    
  });
});


$(document).ready(function() {
  $('#dataTableOrder').DataTable({
    "language": {
      "decimal":        "",
      "emptyTable":     "No hay datos disponibles en la tabla",
      "info":           "Mostrando _START_ a _END_ de _TOTAL_ registros",
      "infoEmpty":      "No hay registros disponibles",
      "infoFiltered":   "(filtrado de _MAX_ registros)",
      "infoPostFix":    "",
      "thousands":      ",",
      "lengthMenu":     "Mostrar _MENU_ registros",
      "loadingRecords": "Cargando ...",
      "processing":     "Procesando ...",
      "search":         "Buscar:",
      "zeroRecords":    "No se encontraron registros",
      "paginate": {
          "first":      "Primero",
          "last":       "Último",
          "next":       "Siguiente",
          "previous":   "Anterior"
      },
      "aria": {
          "sortAscending":  ": activar para ordenar la columna ascendente",
          "sortDescending": ": activar para ordenar la columna descendente"
      }
    },
    "lengthMenu": [ 10, 15, 20, 25 ],
    "order": [[ 1, "asc" ]],
    "pageLength": 15,
    "recordsTotal": 100,
    "recordsFiltered": 100,    
  });
});


$(document).ready(function() {
  $('#dataTableModal').DataTable({
    "info":     false,
    "language": {
      "decimal":        "",
      "emptyTable":     "No hay datos disponibles en la tabla",
      "loadingRecords": "Cargando ...",
      "processing":     "Procesando ...",
      "search":         "Buscar:",
      "paginate": {
          "first":      "<<",
          "last":       ">>",
          "next":       ">",
          "previous":   "<"
      },
    },
    "lengthChange": false,
    "searching": true,
    "ordering": false,
    "paging":   true,
  });
});


$(document).ready(function() {
  $('#dtComerciales').DataTable({
    "info": false,
    "language": {
      "decimal": "",
      "emptyTable": "No hay datos disponibles en la tabla",
      "loadingRecords": "Cargando ...",
    },
    "lengthChange": false,
    "searching": false,
    "order": [[ 1, "asc" ]],
    "paging": false,
  });
});
