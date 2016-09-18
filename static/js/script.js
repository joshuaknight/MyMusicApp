$(document).ready(function(){			
			$("button").on({
			    mouseenter: function(){
			        $("h3").css("background-color", "lightblue");
			    },
			    mouseleave: function(){
			        $("h3").css("background-color", "white");
			    }, 
		    });
		    $("button").click(function(){
		        $("h3").css({"background-color": "blue"});		        
		    });		    
		});