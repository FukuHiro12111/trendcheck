$(() => {
  $("#yahoo").on("click", function () {
    // クリックした要素の ID と違うクラス名のセクションを非表示
    // セクションはボタン id と同じクラス名になっているので、 '.' をつける。
    // $(".section")
    //   .not($("." + $(this).attr("id")))
    //   .hide();
    // クリックした要素の ID と同じクラスのセクションを表示
    // $("." + $(this).attr("id")).show();
    $(".y").remove();
    $(".q").remove();

    // Ajax通信を開始する
    $.ajax({
      type: "GET", // HTTPリクエストメソッドの指定
      dataType: "json", // 受信するデータタイプの指定
      //data: yahoo_button.serialize(), // クエリパラメータの指定。サーバーに送信したいデータを指定
      url: "yahoo/",
      //リクエストが完了するまで実行される
      beforeSend: function () {
        $(".loading").removeClass("hide");
      },
      success: (data) => {
        $(".loading").addClass("hide");
        $("#yahoo-table-body").append(
          '<tr class="y"><th>Yahoo ニュース</th></tr>'
        );
        $.each(data.list, (i, item) => {
          $("#yahoo-table-body").append(
            '<tr class="y" id="' +
              i +
              '"><td><a href="' +
              item[1] +
              '">' +
              item[0] +
              "</a></td></tr>"
          );
        });
        console.log($("#yahoo-table-body"));
      },
      error: () => {
        console.log("失敗", data);
      },
    });
  });
});

$(() => {
  $("#qiita").on("click", () => {
    console.log("id", $("." + $(this).attr("id")));
    $(".y").remove();
    $(".q").remove();

    // Ajax通信を開始する
    $.ajax({
      type: "GET", // HTTPリクエストメソッドの指定
      dataType: "json", // 受信するデータタイプの指定
      //data: yahoo_button.serialize(), // クエリパラメータの指定。サーバーに送信したいデータを指定
      url: "qiita/",
      beforeSend: function () {
        $(".loading").removeClass("hide");
      },
      success: (data) => {
        $(".loading").addClass("hide");
        $("#qiita-table-body").append(
          '<tr class="q"><th>Qiita</th><th></th></tr>'
        );
        $.each(data.list, (i, item) => {
          $("#qiita-table-body").append(
            '<tr class="q" id="' +
              i +
              '"><form action="create/" method="post" id="form_' +
              i +
              '"></form><td><a href="' +
              item[1] +
              '">' +
              item[0] +
              "</a>" +
              '<input type="hidden" name="csrfmiddlewaretoken" value="' +
              "sw0kVuIgyBvRIHnZ0J5X8gNFi1DjftxitV3HewL6UN7P6TV5r82cSxhV0J2kIgJ8" +
              '" form="form_' +
              i +
              '"><input type="hidden" name="title" value="' +
              item[0] +
              '" form="form_' +
              i +
              '"><input type="hidden" name="link" value="' +
              item[1] +
              '" form="form_' +
              i +
              '"></td><td><input type="submit" form="form_' +
              i +
              '" value="保存"></td></tr>'
          );
        });
      },
      error: () => {
        console.log("失敗", data);
      },
    });
  });
});
