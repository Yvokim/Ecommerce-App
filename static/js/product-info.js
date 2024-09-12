var cartAddUrl = document.getElementById('cartAddButton').dataset.cartAddUrl;



    $(document).on('click', '#add-button', function(e){

       e.preventDefault();

       $.ajax({



           type: 'POST',
           url: cartAddUrl,
           data: {

                 product_id:$('#add-button').val(),
                 product_quantity:$('#select option:selected').text(),
                 csrfmiddlewaretoken: csrf_token,
                 action: 'post'


           },

           success: function(json){

                 //console.log(json);

                 document.getElementbyID("cart-qty").textContent=json.qty


           },

           error: function(xhr,errmsg,err){

           }










       }





       )







    })






