(function () {
    // submit maid plan schedule filter form
    $("#scheduleFilterList").on("change", function (e) {
        e.preventDefault();
        $(e.target).closest("form").submit();
    });
})();