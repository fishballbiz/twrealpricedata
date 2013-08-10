function SchoolController($scope, $http) {
  $http.get('api/citylist').success(function(data) {
    $scope.citydata = data;
  });
}
