$(document).ready(function () {

    $('#button').click(function () {
            //createToDoItem() 
        var elem = {id:id, title: $("input[name=title]").val(), active: 'true'}
        var idevent = $('.toogle.change').attr('id') || 'all';
        ajaxAddTodo(elem, idevent);

    });



    $("#content").on('click', '.remove', function () {
        //$('.pages a').removeClass('active');
        //$(this).addClass('active');
        var id = $(this).parent().attr('id');
        var idevent = $('.toogle.change').attr('id') || 'all';
        var strget = window.location.search.replace( '?', '');
        if (strget == '')
            strget = 'None'
        ajaxDelTodo(id,strget,idevent)
         //showItems(false)
         $(this).off() 
    });

  /*  $('.remove').click(function () {
        var id = $(this).parent().attr('id');
        console.log(id);
        ajaxDelTodo(id)
    })*/

    $('input[name=title]').keypress(function(event) {
        if (event.keyCode == 13) {
        var elem = {id:id, title: $("input[name=title]").val(), active: 'true'}
        event.preventDefault();
        ajaxAddTodo(elem, idevent);
        }
    });

    $("#content").on('change', '.todo_item > .checkbox', function() {  
        (this.checked) ? $(this).parent().attr('active', 'false') : $(this).parent().attr('active', 'true')
        var status = $(this).parent().attr('active');
        var id = $(this).parent().attr('id');
        var strget = window.location.search.replace( '?', '');
        if (strget == '')
            strget = 'None'
        var currentpage = ($('.sr-only').attr('id'))
        var idevent = $('.toogle.change').attr('id') || 'all';
        //
        ajaxChangeTodo(status,id,strget, idevent, currentpage) 

    });

      $("#todo").on('dblclick', '.todo_item > span', function() {  
        var _self = this;
        prevContent = $('#todo').html()
        $('.reduction').each(function () {
            
                $(this).replaceWith("<span class='title'>" + $(this).find('input.edit').val() + "</span>")
                if($(this).find('input.edit').val()== '') {
                  alert('Need text')
                  $('#todo').html(prevContent)
                  return
                } 
        });

         $(this).replaceWith("<div class='reduction'><input type='title' class='edit title form-control' value="
         + $(this).text() + " required><a id='save' class='btn btn btn-primary' >Save</a></div>")
         $("li").on('click','.reduction >  a#save', function() {
            prevContent = $('#todo').html()
            var title = $(this).parent().find('input.edit').val()
            if (title == '') {
                alert('Please inter new title')
                $('#todo').html(prevContent)
                return   
            }
            var id = $(this).parent().parent().attr('id');
            
            var currentpage = ($('.sr-only').attr('id'))
            var idevent = $('.toogle.change').attr('id') || 'all';
            ajaxEditTodo(id,title, idevent, currentpage)
         });
      
     });

      $('.todo_item').on('keydown','.reduction > input.edit', function(event) {
            if (event.keyCode == 13) {
                console.log('here')
                
                var text = $(this).closest(".reduction").find('input').val();

                if(text.trim()) {
                    var title = $(this).parent().find('input.edit').val()
                    var id = $(this).parent().parent().attr('id');
                    var currentpage = ($('.sr-only').attr('id'))
                    var idevent = $('.toogle.change').attr('id') || 'all';
                    ajaxEditTodo(id,title, idevent, currentpage)

                } else {
                    alert('Need input some text');

                }
             
            }

        });


    $('.toogle').click(function() {
        $('.toogle').removeClass('change');
        $(this).addClass('change');
        var idevent = $('.toogle.change').attr('id') || 'all';
        ajaxFilterTodo(idevent)
    });

    $('#off').click(function() {
        var idevent = $('.toogle.change').attr('id') || 'all';
        ajaxTodoOff(idevent)
    });

    $('#del').click(function() {
        var idevent = $('.toogle.change').attr('id') || 'all';
        ajaxDellAll(idevent)
    });

     
    // //click on checked or unchecked
    $('#on').click(function() {
        console.log('on')
        var idevent = $('.toogle.change').attr('id') || 'all';
        ajaxTodoOn(idevent)
    });

    $("ul").on('dblclick','li > p', function() {

        $('.reduction').each(function () {
            $(this).replaceWith("<p class='title'>" + $(this).find("input.edit").val() + "</p>")
            if($(this).find("input.edit").val() == '') {
                alert('Need input some text');
               // showItems(false)
            }
        });

        $(this).replaceWith("<div class='reduction'><input type='text' class='edit form-control' value="
         + $(this).text() + "><a id='save' class='btn btn btn-primary' >Save</a></div>");

        $("li").on('click','.reduction >  a#save', function() {
            $(this).off();
            var search = $(this).closest("li").attr('id');
            var text = $(this).closest(".reduction").find('input').val();

            if(text.trim()) {
                for (var i = 0; i < total.length; i++) {
                    if(total[i].id == search) {
                        break;
                    }
                }

        

            } else {
             

            }

           // showItems(false)

        });

        $('li').on('keydown','.reduction > input.edit', function(event) {
            if (event.keyCode == 13) {
                var search = $(this).closest("li").attr('id');
                var text = $(this).closest(".reduction").find('input').val();

                if(text.trim()) {
                    for (var i = 0; i < total.length; i++) {
                        if(total[i].id == search) {
                            break;
                        }

                    }

                    total[i].title = text;
                    //showItems(false)

                } else {
                    alert('Need input some text');

                }
                //showItems(false)

            }

        });

        $(this).off();
       /* showItems(false)*/
    });

});

var total = [];
var count_items = 5;
var count_pages = 1;
var id = 0;

function ajaxDellAll(idevent) {
    $.ajax({
    url: 'del/',
    type: "PUT",
    data: JSON.stringify({idevent}),    //'csrfmiddlewaretoken': '{{ csrf_token }}'
    success: function (response) {
        //console.log(response);
      $('body').html(response); 
    },
    headers: {"X-HTTP-Method-Override": "PUT"},
   })
}

function ajaxTodoOn(idevent) {
    $.ajax({
    url: 'on/',
    type: "PUT",
    data: JSON.stringify({idevent}),    //'csrfmiddlewaretoken': '{{ csrf_token }}'
    success: function (response) {
        //console.log(response);
      $('body').html(response); 
    },
    headers: {"X-HTTP-Method-Override": "PUT"},
   })
}

function ajaxTodoOff(idevent) {
    $.ajax({
    url: 'off/',
    type: "PUT",
    data: JSON.stringify({idevent}),    //'csrfmiddlewaretoken': '{{ csrf_token }}'
    success: function (response) {
        //console.log(response);
      $('body').html(response); 
    },
    headers: {"X-HTTP-Method-Override": "PUT"},
   })
}

function ajaxEditTodo(id,title, idevent, currentpage) {
    $.ajax({
    url: 'update_todo/' + id,
    type: "PUT",
    data: JSON.stringify({id,title,idevent, currentpage}),    //'csrfmiddlewaretoken': '{{ csrf_token }}'
    success: function (response) {
        //console.log(response);
      $('body').html(response); 
    },
    headers: {"X-HTTP-Method-Override": "PUT"},
   })
}

function ajaxFilterTodo(idevent) {
    var url = '' + idevent;
    $.get(url,function(response){
        $('body').html(response);
    })
}

function ajaxChangeTodo(status, id, strget, idevent, currentpage) {
    $.ajax({
    url: 'edit_todo/' + id,
    type: "PUT",
    data: JSON.stringify({status,strget,idevent, currentpage}),    //'csrfmiddlewaretoken': '{{ csrf_token }}'
    success: function (response) {
        //console.log(response);
      $('body').html(response); 
    },
    headers: {"X-HTTP-Method-Override": "PUT"},
   })
}

function ajaxAddTodo(elem, idevent) {
   $.ajax({
    url: 'add_todo/',
    type: "POST",
    data: JSON.stringify([elem,idevent]),     
    success: function (response) {
        //console.log(response);
      $('body').html(response);
      $('input[name=title]').val('');  
      
    }
   })   
}

function ajaxDelTodo(id,strget, idevent) {
   $.ajax({
    url: 'delete/' + id,
    type: "DELETE",
    data: JSON.stringify({id,strget,idevent}),
    headers: { 'X_METHODOVERRIDE': 'DELETE' },     //'csrfmiddlewaretoken': '{{ csrf_token }}'
    success: function (response) {
     $('body').html(response);
    $('input[name=title]').val('');    /*error: function (error) {console.log("Error getting data from the server:", error);}*/
    }
  })   
}
    
function ajaxAllTodo() {
   $.ajax({
    url: '',
    type: "GET",
    data: JSON.stringify(),     //'csrfmiddlewaretoken': '{{ csrf_token }}'
    success: function (response) {
      $('body').html(response);
      
    } 
   })    
}

function  counter(temp) {
    var complete = 0;
    var uncomplete = 0;

    for (var i = 0; i < temp.length; i++) {
        if(temp[i].active == 'true') {
            uncomplete++
        } else {
            complete++
        }

    }

    $('body').find('.uncomplete > span').text(uncomplete);
    $('body').find('.complete > span').text(complete);

    return temp;
}

function createToDoItem() {
    var idevent = $('body').find('.change').attr('id');

    if (!$('input[name=task]').val().trim()) {
        alert('Введите значение');
    } else {
       
        total.push({id:id, title: $("input[name=task]").val(), active: 'true'});
        id++;
    }


    $('input[name=task]').val('');
    event.preventDefault();
    showItems(true)
}

function addPage(arrayLenght, activePage, last) {

    var listPage  = '';
    var myPages = $('.pages');

    count_pages =  Math.ceil(arrayLenght / count_items);

    if (activePage > count_pages || last) {
        activePage = count_pages;
    }

    for (var i = 1; i <= count_pages; i++) {
        var className = (activePage == i) ? 'active' : '';
        listPage += "<a href='#' id=" + i + " class='" + className + "'>" + i + "</a>";
    }

    myPages.html(listPage);

    return activePage;
}

function showItems(last) {         // var basket[] - local array , temp[] - filtered array
    var idevent = $('.toogle.change').attr('id') || 'all';
    var page = $('.pages > a.active').attr('id');
    var listitems = '';
    var temp = total;
    var startIdx;
    var endIdx;
    var slice = [];

    counter(temp)

    if(idevent == 'checked') {
        temp = total.filter(function(i) {
            return i.active == 'false';
        });
    } else if (idevent == 'unchecked') {
        temp = total.filter(function(i) {
            return i.active == 'true';
        });
    }

    page = addPage(temp.length, page, last);

    startIdx = count_items * (page-1);
    endIdx = startIdx + count_items;
    slice = temp.slice(startIdx, endIdx);

    for (var i = 0; i < slice.length; i++) {
        if (i == count_items) break;
        listitems += "<li id=" + slice[i].id + " class='list__item clearfix' active=" + slice[i].active + ">" + "<input type='checkbox'  class='checkbox' " + ((slice[i].active == 'false') ? " checked />" : '>') +
            "<a href='#' class='close' aria-hidden='true'>&times;</a>" +
            "<p class='title'>" + slice[i].title + "</p>" +
            "</li>";
    }

    $('#todo').html(listitems)

}
