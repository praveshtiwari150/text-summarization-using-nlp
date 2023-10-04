$(document).ready(function(){
    $("#submit-btn").click(function(){
        var text = $("#sum").val();
        $ajax({
            url:"/summarize",
            type: "POST",
            data: {text: text},
            success: function(data){
                var audio = new Audio(data);
                audio.play();
            }
        });
    });
});


