odoo.define('web.OdooTest', function (require) {
    "use strict";

    var ListRenderer = require('web.ListRenderer');
    ListRenderer.include({
        _onRowClicked: function () {
            var context = this.state.getContext();
            if (!context['no_open']) {
                this._super.apply(this, arguments);
            }
        }
    })
});