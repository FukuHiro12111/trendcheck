$(() => {
  $("button").click(() => {
    // Ajax通信を開始する
    $.ajax({
      type: "GET",
      url: "yahoo/",
      success: () => {
        console.log("成功");
      },
      error: () => {
        console.log("失敗");
      },
    });
  });
});
