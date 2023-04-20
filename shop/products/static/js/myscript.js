$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml = this.parentNode.children[1]
    console.log("pid =",id)
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data =",data);
            eml.innerText=data.quantity
            document.getElementById("total_price").innerText=data.total_price
            document.getElementById("total_quantity").innerText=data.total_quantity

        }
    })
})


$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml = this.parentNode.children[1]
    console.log("pid =",id)
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data =",data);
            eml.innerText=data.quantity
            document.getElementById("total_price").innerText=data.total_price
            document.getElementById("total_quantity").innerText=data.total_quantity

        }
    })
})


$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id:id
        },
        success:function(data){
            document.getElementById("total_price").innerText=data.total_price
            document.getElementById("total_quantity").innerText=data.total_quantity
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})