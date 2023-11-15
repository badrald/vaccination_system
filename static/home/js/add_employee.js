const successMsg = new bootstrap.Modal(document.getElementById("successMsg"));
const errorMsg = new bootstrap.Modal(document.getElementById("errorMsg"));
const national_num = $("#id_national_number");
jQuery(function () {
  $("#myAlert").hide();
  $.ajaxSetup({
    headers: {
      "X-CSRFToken": "{{ csrf_token }}",
    },
  });
});

$("#upload-file").on("change", function () {
  var filename = $(this).val().split("\\").pop();
  $("#fileStatus").text(filename);
});

$("#addEmployeeForm").on("submit", function (event) {
  event.preventDefault();
  var formData = new FormData(this);
  $.ajax({
    url: "/hr/add_employee/", // Update the URL endpoint
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (data) {
      successMsg.show();
    },
    error: function (error) {
      errorMsg.show();
    },
  });
});

national_num.on("keyup",e => {
  if(national_num.val()[0]=== '2')
      $('#id_sex').val('False');
   else
      $('#id_sex').val('True');
});