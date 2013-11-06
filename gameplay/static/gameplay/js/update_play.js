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
    
    $scope.init = function(){
	
	$scope.currentTurn={background: '#00FFFF'};
	$scope.strikeCount=0;
	$scope.ballCount=0;
	$scope.inningNum=1;
	$scope.numSO=0;
	
	$scope.firstBase='';
	$scope.secondBase='';
	$scope.thirdBase='';
	
	$scope.playerList=playersList;
	$scope.pL=$scope.playerList.length; //Since its used so much
	
	$scope.pitcherList=[];
	$scope.batterList=[];
	for (var i=0;i<$scope.pL;i++){
	    ioff=((i+1) % ($scope.pL));
	    //alert(ioff);
	    pElem={name:$scope.playerList[i]['name'],
		   id:$scope.playerList[i]['id'],
		   turnStyle:{},
		   runsagainst:0};//For ERA computation
	    bElem={name:$scope.playerList[ioff]['name'],
		   id:$scope.playerList[ioff]['id'],
		   turn:1,hits:0,turnStyle:{},
		   sos:0}; //Strikeouts
	    if(i==0){
		pElem.turnStyle=$scope.currentTurn;
		bElem.turnStyle=$scope.currentTurn;
	    }
	    $scope.pitcherList.push(pElem);
	    $scope.batterList.push(bElem);
	}
    };
    
    $scope.getCurrentBatter = function(){
	for (var i=0;i<$scope.pL;i++){
	    if ($scope.batterList[i].turnStyle===$scope.currentTurn){
		return i;
	    }
	}
    };
    
    $scope.getCurrentPitcher = function(){
	for (var i=0;i<$scope.pL;i++){
	    if ($scope.pitcherList[i].turnStyle===$scope.currentTurn){
		return i;
	    }
	}
    };
    
    $scope.updateInning = function(){
	//TODO:
	//1.) Add ajax call to update inning/score/etc. After each inning.
	//2.) Set inning limit.  Return summary page when it's reached:
	//    -->Return loading bar while ajax call fetches summary page.
	$scope.inningNum=$scope.inningNum+1;
	$scope.numSO=0;
    };
    
    $scope.upStrike = function(){
	$scope.strikeCount++;
	if ($scope.strikeCount>=3){
	    $scope.numSO=$scope.numSO+1;
	    var ibat = $scope.getCurrentBatter();
	    var ipitch = $scope.getCurrentPitcher();
	    if ($scope.numSO>=3){
		$scope.pitcherList[ipitch].turnStyle={};
		ipitch=(ipitch+1) % $scope.pL;
		$scope.pitcherList[ipitch].turnStyle=$scope.currentTurn;
		$scope.updateInning();
	    }
	    $scope.batterList[ibat].turnStyle={};
	    $scope.batterList[ibat].turn=$scope.batterList[ibat].turn+1;
	    $scope.batterList[ibat].sos=$scope.batterList[ibat].sos+1;
	    
	    $scope.batterList[ibat].turnStyle={};
	    if($scope.batterList[((ibat+1)%$scope.pL)].name!==
	       $scope.pitcherList[ipitch].name){
		$scope.batterList[((ibat+1)%$scope.pL)].turnStyle=$scope.currentTurn;
	    }else{
		$scope.batterList[((ibat+2)%$scope.pL)].turnStyle=$scope.currentTurn;
	    }
	    $scope.ballCount=0;
	    return $scope.strikeCount=0;
	} else {
	    return $scope.strikeCount;
	}
    };
    $scope.downStrike = function(){
	return $scope.strikeCount--;
    };
    
    $scope.upBall = function(){
	$scope.ballCount++;
	if ($scope.ballCount>=4){
	    var ibat = $scope.getCurrentBatter();
	    var ipitch = $scope.getCurrentPitcher();
	    $scope.pitcherList[ipitch].runsagainst=
		$scope.pitcherList[ipitch].runsagainst+1;
	    $scope.batterList[ibat].hits=$scope.batterList[ibat].hits+1;
	    $scope.batterList[ibat].turn=$scope.batterList[ibat].turn+1;
	    $scope.batterList[ibat].turnStyle={};
	    if($scope.batterList[((ibat+1)%$scope.pL)].name!==
	       $scope.pitcherList[ipitch].name){
		$scope.batterList[((ibat+1)%$scope.pL)].turnStyle=$scope.currentTurn;
	    }else{
		$scope.batterList[((ibat+2)%$scope.pL)].turnStyle=$scope.currentTurn;
	    }
	    $scope.strikeCount=0;
	    return $scope.ballCount=0;
	} else
	    return $scope.ballCount;
    };
    
    $scope.downBall = function(){
	return $scope.ballCount--;
    };
    
    $scope.score = function(amt){
	var ipitch = $scope.getCurrentPitcher();
	$scope.pitcherList[ipitch].runsagainst=$scope.pitcherList[ipitch].runsagainst+amt;
	var ibat = $scope.getCurrentBatter();
	$scope.batterList[ibat].hits=$scope.batterList[ibat].hits+amt;
	$scope.batterList[ibat].turn=$scope.batterList[ibat].turn+1;
	$scope.batterList[ibat].turnStyle={};
	if($scope.batterList[((ibat+1)%$scope.pL)].name!==
	   $scope.pitcherList[ipitch].name){
	    $scope.batterList[((ibat+1)%$scope.pL)].turnStyle=$scope.currentTurn;
	}else{
	    $scope.batterList[((ibat+2)%$scope.pL)].turnStyle=$scope.currentTurn;
	}
	$scope.strikeCount=0;
	$scope.ballCount=0;
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

    $scope.init();
}
