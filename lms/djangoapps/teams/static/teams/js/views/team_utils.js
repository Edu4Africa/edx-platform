/*  Team utility methods*/
;(function (define) {
    'use strict';
    define([
        'backbone'
    ], function (Backbone) {
        return _.extend(Backbone.View.prototype, {

            /**
             * Convert a 2d array to an object equivalent with an additional blank element
             *
             * @param options {Array.<Array.<string>>} Two dimensional options array
             * @returns {Object} Hash version of the input array
             * @example selectorOptionsArrayToHashWithBlank([["a", "alpha"],["b","beta"]])
             * // returns {"a":"alpha", "b":"beta", "":""}
             */
            selectorOptionsArrayToHashWithBlank: function (options) {
                var map = _.object(options);
                map[""] = "";
                return map;
            }
        });

    });

}).call(this, define || RequireJS.define);
