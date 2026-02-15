// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "hardhat/console.sol";

contract RoyaltySplitter {
    struct Payee {
        address account;
        uint256 shares;
    }

    Payee[] public payees;
    uint256 public totalShares;
    mapping(address => uint256) public shares;

    event PaymentReleased(address to, uint256 amount);
    event PayeeAdded(address account, uint256 shares);
    event PaymentReceived(address from, uint256 amount);

    constructor() {}

    receive() external payable {
        emit PaymentReceived(msg.sender, msg.value);
    }

    /**
     * @dev Add a new payee to the contract.
     * @param account The address of the payee to add.
     * @param shares_ The number of shares owned by the payee.
     */
    function addPayee(address account, uint256 shares_) public {
        require(account != address(0), "RoyaltySplitter: account is the zero address");
        require(shares_ > 0, "RoyaltySplitter: shares are 0");
        require(shares[account] == 0, "RoyaltySplitter: account already has shares");

        payees.push(Payee(account, shares_));
        shares[account] = shares_;
        totalShares = totalShares + shares_;
        emit PayeeAdded(account, shares_);
    }

    /**
     * @dev Update shares based on contribution map from AI.
     * simplified for demonstration. Ideally this would be controlled by a DAO or Oracle.
     * @param accounts Array of addresses to update/add.
     * @param newShares Array of new share amounts.
     */
    function updateContributions(address[] memory accounts, uint256[] memory newShares) public {
        require(accounts.length == newShares.length, "RoyaltySplitter: length mismatch");
        
        // Resetting shares logic is complex in production (handling pending payments).
        // This is a simplified version for the hackathon/demo context.
        for (uint256 i = 0; i < accounts.length; i++) {
            address account = accounts[i];
            uint256 share = newShares[i];
            
            if (shares[account] > 0) {
                 totalShares = totalShares - shares[account] + share;
                 shares[account] = share;
            } else {
                addPayee(account, share);
            }
        }
    }

    /**
     * @dev Distribute funds to all payees based on their shares.
     */
    function distribute() public {
        uint256 balance = address(this).balance;
        require(balance > 0, "RoyaltySplitter: no funds to distribute");
        
        for (uint256 i = 0; i < payees.length; i++) {
            address account = payees[i].account;
            uint256 share = shares[account];
            uint256 payment = (balance * share) / totalShares;
            
            payable(account).transfer(payment);
            emit PaymentReleased(account, payment);
        }
    }
}
