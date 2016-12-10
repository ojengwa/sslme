app.controller("RegisterController", [
    "$scope",
    "$location",
    "$log",
    "$localStorage",
    "$sessionStorage",
    "$rootScope",
    "Request",
    function ($scope, $location, $log, $localStorage, $sessionStorage, $rootScope, Request) {
        'use strict';

        if (!$localStorage.domain) {
            $location.path('/login');
        };

        $scope.data = {};

        $scope.register = function () {
            $scope.message = null;
            console.log($scope.data);
            $scope.data.domain = $localStorage.domain.host;
            var errCode;
            Request.fetch('users', $scope.data)
                .then(function (res) {
                    $sessionStorage.auth = res.auth;
                    $localStorage.auth = res.auth;
                    $localStorage.user = res.data;
                    $rootScope.user = $localStorage.user;
                    $location.path('/dashboard')
                }, function (error) {
                    console.log(error);

                    errCode = error.code.split('_').join(' ');
                    $scope.errCode = errCode.substring(0, 1).toUpperCase() + errCode.substring(1).toLowerCase() + "!";
                    $scope.message = error.message;
                    console.log(errCode, $scope.errCode, $scope.message);
                });

        }
        $log.debug("Register Controller Initialized");
    }]);