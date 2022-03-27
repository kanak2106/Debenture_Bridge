// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.22 <0.8.0;
contract transaction{
    struct _transaction{
        string _lender;
        string _borrower;
        uint _amount;
        uint _dueDate;
        uint _id;
        uint _rating;
    }
     _transaction[] public transactionDetail;
     uint _min_lended_amount = 500;

     function transact(string memory _lender, string memory _borrower, uint _amount, uint _dueDate, uint _id, uint _rating)public {
          transactionDetail.push( _transaction(_lender,_borrower,_amount,_dueDate,_id,_rating));

     }

     function _moneyLended( uint _amount ) public view returns(string memory){
        if(_min_lended_amount <= _amount){
            return "Congrats!! Transaction Done Successfully.";
        }
        else {
            return "Transaction not supported , Try Again. ";
        }

     }

 


}