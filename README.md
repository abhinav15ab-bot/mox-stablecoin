# 🪙 MOX StableCoin Protocol

> A Decentralized Over-Collateralized Stablecoin built with Vyper, Solidity & Python  
> Designed for learning DeFi architecture, collateral management, and smart contract security.

---

## 📌 Overview

MOX StableCoin is a decentralized, over-collateralized stablecoin protocol inspired by MakerDAO-style systems.

Users can:

- 🏦 Deposit collateral (e.g., ETH / ERC20 tokens)
- 🪙 Mint MOX stablecoins against their collateral
- 💥 Get liquidated if under-collateralized
- 🔒 Maintain system stability through collateral ratio enforcement

The protocol ensures that every MOX token is backed by more value than it represents.

---

## 🧠 How It Works (High-Level Flow)

1. User deposits collateral into the protocol.
2. Protocol calculates the USD value of the collateral.
3. User mints MOX within safe collateral limits.
4. Health Factor is continuously checked.
5. If collateral value drops below threshold → liquidation occurs.
6. User can burn MOX to withdraw collateral.

---

## 🏗️ Architecture

```
User
 │
 ▼
Collateral Deposit
 │
 ▼
MOX Engine (Core Logic)
 │
 ├── Collateral Management
 ├── Mint / Burn Logic
 ├── Health Factor Calculation
 └── Liquidation System
 │
 ▼
MOX StableCoin Token Contract
```

---

## 📂 Project Structure

```
mox-stablecoin/
│
├── contracts/
│   ├── MOXStableCoin.vy        # ERC20 Stablecoin (Vyper)
│   ├── MOXEngine.sol           # Core protocol logic
│   └── Interfaces/             # Required interfaces
│
├── script/
│   ├── Deploy.s.sol            # Deployment scripts
│
├── test/
│   ├── MOXTest.t.sol           # Unit tests
│
├── lib/                        # Dependencies
│
└── foundry.toml                # Foundry configuration
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| 🟢 Vyper | Stablecoin token contract |
| 🟣 Solidity | Core engine logic |
| 🐍 Python | Testing / scripting |
| ⚙️ Foundry | Development & testing framework |
| 🧪 Forge | Smart contract testing |
| 📡 Anvil | Local blockchain |

---

## 🔐 Key Concepts Implemented

- ✅ Over-collateralization
- ✅ Health factor calculation
- ✅ Liquidation mechanism
- ✅ Price feed integration (Chainlink style)
- ✅ Decentralized minting
- ✅ Burn-to-withdraw model

---

## 📊 Core Functions

### Deposit Collateral
```solidity
depositCollateral(address token, uint256 amount)
```

### Mint MOX
```solidity
mintMox(uint256 amount)
```

### Burn MOX
```solidity
burnMox(uint256 amount)
```

### Liquidate
```solidity
liquidate(address user)
```

---

## 🧮 Health Factor Formula

```
Health Factor = (Collateral Value * Liquidation Threshold) / Minted MOX
```

If:

- Health Factor > 1 → Safe ✅  
- Health Factor < 1 → Eligible for liquidation ⚠️  

---

## 🚀 Getting Started

### 1️⃣ Install Foundry
```bash
curl -L https://foundry.paradigm.xyz | bash
foundryup
```

### 2️⃣ Clone Repository
```bash
git clone https://github.com/your-username/mox-stablecoin.git
cd mox-stablecoin
```

### 3️⃣ Install Dependencies
```bash
forge install
```

### 4️⃣ Build Contracts
```bash
forge build
```

### 5️⃣ Run Tests
```bash
forge test -vv
```

### 6️⃣ Deploy Locally
```bash
anvil
forge script script/Deploy.s.sol --rpc-url http://127.0.0.1:8545 --broadcast
```

---

## 🔍 Data Flow Explanation

```
User → Deposit Collateral
      → Collateral Value Stored
      → Mint MOX (checked against health factor)
      → MOX Token Minted
      → System tracks debt
```

On price drop:

```
Collateral Value ↓
Health Factor < 1
→ Liquidator repays debt
→ Liquidator receives collateral bonus
```

---

## 🎯 Why This Project?

This project helps understand:

- DeFi protocol architecture
- Stablecoin mechanics
- Risk management
- Liquidation models
- Smart contract security
- Vyper vs Solidity comparison

---

## 🧪 Testing Philosophy

- Unit tests for every core function
- Revert testing for invalid scenarios
- Edge case testing for liquidation logic
- Health factor boundary tests

---

## 📈 Future Improvements

- 🔮 Governance mechanism
- 🌐 Frontend dashboard
- 🧾 On-chain parameter updates
- 🛡️ Advanced security auditing
- 📊 Dynamic collateral types

---

## ⚠️ Disclaimer

This project is built for educational purposes.  
Do NOT use in production without professional auditing.

---

## 👨‍💻 Author

Built by **Abhinav Malik**  
B.Tech ECE | Blockchain Developer | DeFi Enthusiast  

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub and share your feedback!




# Stablecoin

1. Users can deposit $200 of ETH
2. They can then mint $50 of stablecoin
   1. This means they will have 4/1 ratio of collateral to stablecoin (200/50 == 4/1)
   2. We will set a requires collateral ratio of 2/1
3. If the price of ETH drops, for example to $50, others should be able to liquidate those users!

