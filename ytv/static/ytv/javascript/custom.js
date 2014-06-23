$(document).ready(function(){
    $('#post_form').submit(function()
    {
        var yturl = $('#yturl').val()
        var post_data = '{"url":"'+yturl+'"}'
        var url = $('#post_form').attr("action")
        $('#wait').show()
        $.post(url, post_data, callback_post, "json")
        return false;
    });
    $('#video_list').on("click", ".delete_link", delete_video)
    $('#wait').hide()
    return;
});

var delete_video = function(e)
{
    var post_data = '{"_method":"DELETE"}'
    var url = e.target.getAttribute("href")
    $('#wait').show()
    $.post(url, post_data, callback_delete, "json")
    return false;
}

var callback_delete = function(data)
{
    if(data.response)
    {
        var id = "#"+data.response
        $(id).remove()
    }

    if(data.messages)
    {
        $('#messages').empty()
        $('#messages').append(data.messages)
    }
    $('#wait').hide()
}

var callback_post = function(data)
{
    if(data.response)
    {
        $('#holder').remove()
        var s = $('#video_list').children().size()
        if(s > 9)
        {
            $('#video_list li:last').remove()
        }
        $('#video_list').prepend(data.response)
        $('#yturl').val('')
    }
    
    if(data.messages)
    {
        $('#messages').empty()
        $('#messages').append(data.messages)
    }

    if(data.paginate)
    {
        $('#step-links').empty()
        $('#step-links').append(data.paginate)
    }
    $('#wait').hide()
}

function getCookie(name)
{
    var cookieValue = null;
    if (document.cookie && document.cookie != '')
    {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++)
        {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '='))
            {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken')

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
