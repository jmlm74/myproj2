"use strict";
console.log("base corejs loaded !");

/***********************************/
/* For compatibility with tables2  */
/* can't set redirection in table  */
/* --> build url here for bs-modal */
/***********************************/
// Display bs-modal
if (typeof formURLDisplay !== 'undefined'){
    $(".Display-class").each(function () {
        let url=formURLDisplay+$(this).attr('id');
        url = url.slice(0,-1);  // remove last caracter idU to get the id
        $(this).modalForm({
            formURL: url,
            modalID: "#modal"
        });
    });
}
// Update bs-modal
if (typeof formURLUpdate !== 'undefined'){
    $(".Update-class").each(function () {
        let url=formURLUpdate+$(this).attr('id');
        url = url.slice(0,-1);  // remove last caracter idU to get the id
        $(this).modalForm({
            formURL: url,
            modalID: "#create-modal"
        });
    });
}
// Remove bs-modal
if (typeof formURLRemove !== 'undefined'){
    $(".Remove-class").each(function () {
        let url=formURLRemove+$(this).attr('id');
        url = url.slice(0,-1);  // remove last caracter idU to get the id
        $(this).modalForm({
            formURL: url,
            modalID: "#create-modal"
        });
    });
}
$(".bs-modal-large").each(function () {
    $(this).modalForm(
        {
            formURL: $(this).data("form-url"),
            modalID: "#modal-large"
        });
});

$(".bs-modal").each(function () {
    $(this).modalForm(
        {
            formURL: $(this).data("form-url"),
            modalID: "#modal"
        });
});


