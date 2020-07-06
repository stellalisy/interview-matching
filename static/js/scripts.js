$("form[name=signup_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/dashboard/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=login_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/dashboard/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});


$("form[name=interviewer_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/interviewer/update",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/success/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=interviewee_form").submit(function(e) {
  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/interviewee/update",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/success/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=admin_form").submit(function(e) {
  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/admin/update",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/success/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});


var cols = 3;
var rows = 10;
var content = "";
var num = 1;
for (var i = 0; i <= rows; i++) {
  for (var j = 0; j <= cols; j++) {
    if (j === 0) {;
      time_slot = i;
      if (i === 0){
        content += "<div class='row'><div style='text-align:center;background:#FFFFFF;color:#000000' class='grid_label'></div>";
      } else {
      content += "<div class='row'><div style='text-align:center;background:#FFFFFF;color:#000000' class='grid_label'>" + "time " + time_slot + "</div>";
      }
    } else if (j === cols) {
      if (i === 0){
        day = j;
        content += "<div style='text-align:center;background:#FFFFFF;color:#000000' class='grid_label'>" + "Day " + day +  "</div></div>";
      }
      else {
        num = (j-1) * rows + i;
        content += "<div style='text-align:center;' class='grid'>" + num +  "</div></div>";
      }
    } else {
      if (i === 0){
        day = j;
        content += "<div style='text-align:center;background:#FFFFFF;color:#000000' class='grid_label'>" + "Day " + day +  "</div>";
      }
      else {
        num = (j-1) * rows + i;
        content += "<div style='text-align:center;' class='grid'>" + num +  "</div>";
      }
    }
  }
}
$("#grids").html(content);

$("#grids").on("click", ".grid", function() {
  var value = $(this).text();
  setColor(event);
});

function setColor(e) {
  var target = e.target,
      count = +target.dataset.count;
   target.style.backgroundColor = count === 1 ? "#adade4" : '#c2e4ad';
   target.dataset.count = count === 1 ? 0 : 1;
}
