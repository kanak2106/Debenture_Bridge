// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.22 <0.8.0;
contract Login{
 struct Member{
     uint id;
 string name; // can also use bytes32 ---> 32 length of string
 string email;
 string gender;
  uint age;
  uint  pan;
  uint adhar;
  uint   contact;
 }
  Member[] public member;
  uint totalMember =1;
  
  //============================= Register New-User ========================================================
function registerNewUser(string memory name, string memory email, string memory gender, uint age, uint pan, uint UserAdhar, uint  contact)  public {
  member.push(Member(totalMember,name,email,gender,age,pan, UserAdhar,contact));
  totalMember++;
 
}
//========================== Login existing user via adhar================================================
function loginUser(uint  _adhar) public  view returns (string memory){
bool i = checkAdhar( _adhar);
if(i){
return "Login successfully";
}else{
    return "Login Failed";
}
}
//============================ delete the user ===========================================================
function deleteUser(uint _id) public {
  uint i = checkMember(_id);
  delete member[i];
} 
 
//============================== Update the user profile =================================================
function updateUser(uint _id,string memory _name, string memory  _email, string memory _gender, uint _age, uint _pan, uint _adhar, uint  _contact) public  {
  uint i = checkMember(_id);
  member[i].name =  _name;
  member[i].adhar =   _adhar;
  member[i].gender = _gender; 
  member[i].age = _age;
  member[i].email = _email;
  member[i].pan = _pan;
  member[i].contact = _contact;
}
// ==================== Comapare functions =====================================
    function checkMember(uint256 _sid) internal view returns (uint256) {
        for (uint256 i = 0; i <  member.length; i++) {
            if (member[i].id == _sid) {
                return i;
            }
        }
        revert(" Member Does not Exist");
    }
     function checkAdhar(uint256 _aadhar) internal view returns (bool) {
        for (uint256 i = 0; i <  member.length; i++) {
            if (member[i].adhar == _aadhar) {
                return true;
            }
        }
        return false;
        
    }
// ============================get Total Members ====================================
function getTotalMembers( ) public view returns (uint length){
 return member.length;
}
}