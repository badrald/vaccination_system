const successMsg = new bootstrap.Modal(document.getElementById("successMsg"));
const errorMsg = new bootstrap.Modal(document.getElementById("errorMsg"));
jQuery(function () {
  $.ajaxSetup({
    headers: {
      "X-CSRFToken": "{{ csrf_token }}",
    },
  });
});


$("#addJobPlacement").on("submit", function (e) {
  e.preventDefault();
  var formData = new FormData(this);
  $.ajax({
    url: addUrl,
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (data) {
      let showJobPlacement = $("#showJobPlacement");
      showJobPlacement.attr("href",`/hr/job_placement/Show/${data.id}`);
      successMsg.show();
    },
    error: function (error) {
      errorMsg.show();
    },
  });
});

