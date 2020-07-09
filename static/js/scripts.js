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


// $("form[name=interviewer_form").submit(function(e) {

//   var $form = $(this);
//   var $error = $form.find(".error");
//   var data = $form.serialize();

//   $.ajax({
//     url: "/interviewer/update",
//     type: "POST",
//     data: data,
//     dataType: "json",
//     success: function(resp) {
//       window.location.href = "/success/";
//     },
//     error: function(resp) {
//       $error.text(resp.responseJSON.error).removeClass("error--hidden");
//     }
//   });

//   e.preventDefault();
// });

// $("form[name=interviewee_form").submit(function(e) {
//   var $form = $(this);
//   var $error = $form.find(".error");
//   var data = $form.serialize();

//   $.ajax({
//     url: "/interviewee/update",
//     type: "POST",
//     data: data,
//     dataType: "json",
//     success: function(resp) {
//       window.location.href = "/success/";
//     },
//     error: function(resp) {
//       $error.text(resp.responseJSON.error).removeClass("error--hidden");
//     }
//   });

//   e.preventDefault();
// });

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


// var cols = 3 + 1;
// var rows = 10 + 1;
// var content = "";
// var num = 1;
// for (var i = 1; i <= rows; i++) {
//   for (var j = 1; j <= cols; j++) {
//     if (j === 1) {;
//       time_slot = i - 1;
//       if (i === 1){
//         content += "<div class='row'><div style='text-align:center;background:#FFFFFF;color:#000000' class='grid_label'></div>";
//       } else {
//       content += "<div class='row'><div style='text-align:center;background:#FFFFFF;color:#000000' class='grid_label'>" + "time " + time_slot + "</div>";
//       }
//     } else if (j === cols) {
//       if (i === 1){
//         day = j - 1;
//         content += "<div style='text-align:center;background:#FFFFFF;color:#000000' class='grid_label'>" + "Day " + day +  "</div></div>";
//       }
//       else {
//         num = (j-2) * (rows - 1) + i - 1;
//         content += "<div style='text-align:center;' class='grid'>" + num +  "</div></div>";
//       }
//     } else {
//       if (i === 1){
//         day = j - 1;
//         content += "<div style='text-align:center;background:#FFFFFF;color:#000000' class='grid_label'>" + "Day " + day +  "</div>";
//       }
//       else {
//         num = (j-2) * (rows - 1) + i - 1;
//         content += "<div style='text-align:center;' class='grid'>" + num +  "</div>";
//       }
//     }
//     //num++;
//   }
// }
// $("#grids").html(content);

// $("#grids").on("click", ".grid", function() {
//   var value = $(this).text();
//   setColor(event);
// });

// function setColor(e) {
//   var target = e.target,
//       count = +target.dataset.count;

//    target.style.backgroundColor = count === 1 ? "#adade4" : '#c2e4ad';
//    target.dataset.count = count === 1 ? 0 : 1;
//    /* 

//    () : ? - this is conditional (ternary) operator - equals 

//    if (count === 1) {
//       target.style.backgroundColor = "#7FFF00";
//       target.dataset.count = 0;
//    } else {
//       target.style.backgroundColor = "#FFFFFF";
//       target.dataset.count = 1;
//    } 
//    target.dataset - return all "data attributes" for current element, 
//    in the form of object, 
//    and you don't need use global variable in order to save the state 0 or 1
//   */ 
// }
