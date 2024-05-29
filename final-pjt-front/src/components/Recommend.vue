<template>
  <div class="financial-calculator">
    <h1>Financial Calculator</h1>

    <div>
      <h2>Simple Interest (예금)</h2>
      <label for="principal">Principal (원금): </label>
      <input v-model.number="principal" id="principal" type="number" />

      <label for="rate">Annual Interest Rate (이율, %): </label>
      <input v-model.number="rate" id="rate" type="number" />

      <label for="years">Years (기간): </label>
      <input v-model.number="years" id="years" type="number" />

      <button @click="calculateSimpleInterest">Calculate</button>
      <p>Total Amount (단리): {{ simpleInterestResult }}</p>
    </div>

    <div>
      <h2>Compound Interest (복리 예금)</h2>
      <label for="compoundPrincipal">Principal (원금): </label>
      <input v-model.number="compoundPrincipal" id="compoundPrincipal" type="number" />

      <label for="compoundRate">Annual Interest Rate (이율, %): </label>
      <input v-model.number="compoundRate" id="compoundRate" type="number" />

      <label for="compoundYears">Years (기간): </label>
      <input v-model.number="compoundYears" id="compoundYears" type="number" />

      <label for="compoundFrequency">Compounding Frequency (연간 횟수): </label>
      <input v-model.number="compoundFrequency" id="compoundFrequency" type="number" />

      <button @click="calculateCompoundInterest">Calculate</button>
      <p>Total Amount (복리): {{ compoundInterestResult }}</p>
    </div>

    <div>
      <h2>Regular Deposit (단리 적금)</h2>
      <label for="monthlyDeposit">Monthly Deposit (월 납입금액): </label>
      <input v-model.number="monthlyDeposit" id="monthlyDeposit" type="number" />

      <label for="depositRate">Annual Interest Rate (이율, %): </label>
      <input v-model.number="depositRate" id="depositRate" type="number" />

      <label for="depositYears">Years (기간): </label>
      <input v-model.number="depositYears" id="depositYears" type="number" />

      <button @click="calculateRegularDeposit">Calculate</button>
      <p>Total Amount (단리 적금): {{ regularDepositResult }}</p>
    </div>

    <div>
      <h2>Regular Deposit (복리 적금)</h2>
      <label for="compoundMonthlyDeposit">Monthly Deposit (월 납입금액): </label>
      <input v-model.number="compoundMonthlyDeposit" id="compoundMonthlyDeposit" type="number" />

      <label for="compoundDepositRate">Annual Interest Rate (이율, %): </label>
      <input v-model.number="compoundDepositRate" id="compoundDepositRate" type="number" />

      <label for="compoundDepositYears">Years (기간): </label>
      <input v-model.number="compoundDepositYears" id="compoundDepositYears" type="number" />

      <label for="compoundDepositFrequency">Compounding Frequency (연간 횟수): </label>
      <input v-model.number="compoundDepositFrequency" id="compoundDepositFrequency" type="number" />

      <button @click="calculateCompoundRegularDeposit">Calculate</button>
      <p>Total Amount (복리 적금): {{ compoundRegularDepositResult }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // 단리 예금
      principal: 0,
      rate: 0,
      years: 0,
      simpleInterestResult: 0,

      // 복리 예금
      compoundPrincipal: 0,
      compoundRate: 0,
      compoundYears: 0,
      compoundFrequency: 1,
      compoundInterestResult: 0,

      // 단리 적금
      monthlyDeposit: 0,
      depositRate: 0,
      depositYears: 0,
      regularDepositResult: 0,

      // 복리 적금
      compoundMonthlyDeposit: 0,
      compoundDepositRate: 0,
      compoundDepositYears: 0,
      compoundDepositFrequency: 1,
      compoundRegularDepositResult: 0,
    };
  },
  methods: {
    calculateSimpleInterest() {
      const P = this.principal;
      const r = this.rate / 100;
      const t = this.years;
      this.simpleInterestResult = P * (1 + r * t);
    },
    calculateCompoundInterest() {
      const P = this.compoundPrincipal;
      const r = this.compoundRate / 100;
      const t = this.compoundYears;
      const n = this.compoundFrequency;
      this.compoundInterestResult = P * Math.pow((1 + r / n), n * t);
    },
    calculateRegularDeposit() {
      const M = this.monthlyDeposit;
      const r = this.depositRate / 100;
      const t = this.depositYears;
      const n = t * 12;
      this.regularDepositResult = M * n + M * n * (n + 1) / 24 * r;
    },
    calculateCompoundRegularDeposit() {
      const M = this.compoundMonthlyDeposit;
      const r = this.compoundDepositRate / 100;
      const t = this.compoundDepositYears;
      const n = t * 12;
      const compoundFactor = (Math.pow(1 + r / 12, n) - 1) / (r / 12);
      this.compoundRegularDepositResult = M * compoundFactor;
    }
  }
};
</script>

<style scoped>
.financial-calculator {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background: #f9f9f9;
}

h1, h2 {
  text-align: center;
}

label {
  display: block;
  margin-top: 10px;
}

input {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
}

button {
  display: block;
  width: 100%;
  padding: 10px;
  margin-top: 20px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background: #0056b3;
}
</style>
