import {SendAjax, getCookie, test2} from '../../../../static/js/modul.js'


/* *********************** */
/* * Beginning Modal box * */
/* *********************** */
if ((document.getElementById('mgrmgmt')) || (document.getElementById('main'))) {    // manager page
    //JQuery is used for BSModal (Bootstrap)
        $(function () {
            console.log("Jquery loaded!!!!!")
            
            $("#createUtilisateur").modalForm({
                formURL: formURLCreate,
                modalID: "#create-modal"
            });
   
        });
   
    }
/* ********************* */
/* * Beginning end box * */
/* ********************* */