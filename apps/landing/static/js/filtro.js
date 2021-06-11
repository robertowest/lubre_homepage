$(document).ready(function() {
    // agregamos la clase active al primer enlace
    $('.category_list .category_item[category="all"]').addClass('ct_item-active');

    // filtro de productos
    $('.category_item').click(function(){
        var catProduct = $(this).attr('category');
        console.log(catProduct);

        alert(catProduct); 

        // agregamos la clase active al enlace seleccionado
        $('.category_item').removeClass('ct_item-active');
        $(this).addClass('ct_item-active');

        // ocultamos los productos de otras categorías (grupos)
        $('.product-item').css('transform', 'scale(0)');
        function hideProduct(){
            $('.product-item').hide();
        } setTimeout(hideProduct,400);

        // visualizamos los productos de la categoría (grupo) seleccionada
        function showProduct(){
            $('.product-item[category="'+catProduct+'"]').show();
            $('.product-item[category="'+catProduct+'"]').css('transform', 'scale(1)');
        } setTimeout(showProduct,400);
    });

    // mostramos todos los productos
    $('.category_item[category="all"]').click(function(){
        function showAll(){
            $('.product-item').show();
            $('.product-item').css('transform', 'scale(1)');
        } setTimeout(showAll,400);
    });
});