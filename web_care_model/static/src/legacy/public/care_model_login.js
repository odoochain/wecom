odoo.define("web_care_model.login", function (require) {
  "use strict";

  const publicWidget = require("web.public.widget");
  var core = require("web.core");
  var QWeb = core.qweb;
  var _t = core._t;
  var _lt = core._lt;

  publicWidget.registry.LoginCareModel = publicWidget.Widget.extend({
    selector: ".oe_login_form",
    // xmlDependencies: ['/wecom_auth_oauth/static/src/xml/providers.xml'],
    events: {
      "click button.toggle_care_mode": "_onToggleModel",
    },
    init: function () {
      this._super.apply(this, arguments);
    },
    start: function () {
      var self = this;
      this.add_care_mode_button();
      this.init_care_mode();
      return this._super.apply(this, arguments);
    },
    init_care_mode: function () {
      var careModel = window.localStorage.getItem("care_mode");
      if (careModel) {
        this.$el.addClass("login_care_mode");
        $(this.login_button).addClass("btn-lg");
      }
    },
    add_care_mode_button: function () {
      this.care_button = $(
        "<button class='btn btn-outline-success btn-lg toggle_care_mode'></button>"
      );
      this.care_button.text(_lt("Enable Care Mode"));
      this.login_button = this.$el.find("button[type='submit']")[0];
      $(this.login_button).after(this.care_button);
    },
    _onToggleModel: function (ev) {
      ev.preventDefault();
      ev.stopPropagation();
      console.log($(ev.currentTarget));
      if (!this.$el.hasClass("login_care_mode")) {
        this.$el.addClass("login_care_mode");
        $(this.login_button).addClass("btn-lg");;
        this.care_button.text(_lt("Disable Care Mode"));
        window.localStorage.setItem("care_mode", true);
      } else {
        this.$el.removeClass("login_care_mode");
        $(this.login_button).removeClass("btn-lg");
        this.care_button.text(_lt("Enable Care Mode"));
        window.localStorage.setItem("care_mode", false);
      }
    },
  });
});
