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


var cols = 3 + 1;
var rows = 10 + 1;
var content = "";
var num = 1;
for (var i = 1; i <= rows; i++) {
  for (var j = 1; j <= cols; j++) {
    if (j === 1) {
      num = (j-1) * cols + i;
      content += "<div style='text-align:center;' class='row'><div class='grid'>" + num + "</div>";
    } else if (j === cols) {
      num = (j-1) * cols + i;
      content += "<div style='text-align:center;' class='grid'>" + num + "</div></div>";
    } else {
      num = (j-1) * cols + i;
      content += "<div style='text-align:center;' class='grid'>" + num + "</div>";
    }
    //num++;
  }
}
$("#grids").html(content);
