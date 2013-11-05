function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Logic Will proceed as follows:

// Page loads, with given batter/pitcher turn variable

// Branch according to stikeout, walk, 1, 2, 3, 4

// if strikeout:
// --> Increment strikeouts by 1
// --> Send score, battern turn, inning
// if walk:
// --> send score, batter turn, inning
function updateAtBat($scope,$http){
    $scope.strikeCount=0;
    $scope.ballCount=0;
    $scope.inningNum=1;
    $scope.numSO=0;
    
    $scope.firstBase='';
    $scope.secondBase='';
    $scope.thirdBase='';
    $scope.playerLList=playersList;
    
    $scope.upStrike = function(){
	return $scope.strikeCount++;
    };
    $scope.downStrike = function(){
	return $scope.strikeCount--;
    };
    
    $scope.upBall = function(){
	$scope.ballCount++;
	if ($scope.ballCount>=4){
	    $scope.firstBase='YES'//'<i class="icon-ok"></i>';
	    return $scope.ballCount=0;
	} else
	    return $scope.ballCount;
    };
    
    $scope.downBall = function(){
	return $scope.ballCount--;
    };
    
    $scope.single = function(){
	
    };
    $scope.test = function(){
	var csrftoken = getCookie('csrftoken');
	var myData=[{'item1':1,'item2':2 },{'obj2':3},];
	
	$http({
		method:'POST',
		    url:'',
		    data:myData,
		    headers:{"X-CSRFToken":csrftoken}
	    }).success(function(data, status, headers, config){
		    alert(data);
		} );
    };
    
    //$scope.2ouble = function(){
    //
    //};
    
    //$scope.triple = function(){
    //};
       
    
}
