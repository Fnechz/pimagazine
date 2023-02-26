interface PaymentDTO {
  amount: number,
  user_uid: string,
  created_at: string,
  identifier: string,
  metadata: Object,
  memo: string,
  status: {
    developer_approved: boolean,
    transaction_verified: boolean,
    developer_completed: boolean,
    cancelled: boolean,
    user_cancelled: boolean,
  },
  to_address: string,
  transaction: null | {
    txid: string,
    verified: boolean,
    _link: string,
  },
};

type AuthResult = {
  accessToken: string,
  user: {
    uid: string,
    username: string
  }
};
type MyPaymentMetadata = {};
export{};
// const [user, setUser] = useState<User | null>(null);
// const [showModal, setShowModal] = useState<boolean>(false);

  const signIn = async () => {
    const scopes = ['username', 'payments'];
    const authResult: AuthResult = await window.Pi.authenticate(scopes, onIncompletePaymentFound);
    signInUser(authResult);
    //setUser(authResult.user);
  }

  const signOut = () => {
    //setUser(null);
    signOutUser();
  }

  const signInUser = (authResult: AuthResult) => {
    //axiosClient.post('/user/signin', {authResult});
    //return setShowModal(false);
  }

  const signOutUser = () => {
    //return axiosClient.get('/user/signout');
  }

  const onModalClose = () => {
    //setShowModal(false);
  }

  const orderProduct = async (memo: string, amount: number, paymentMetadata: MyPaymentMetadata) => {
    // if(user === null) {
    //   return setShowModal(true);
    // }
    const paymentData = { amount, memo, metadata: paymentMetadata };
    const callbacks = {
      onReadyForServerApproval,
      onReadyForServerCompletion,
      onCancel,
      onError
    };
    const payment = await window.Pi.createPayment(paymentData, callbacks);
    console.log(payment);
  }

  //my additions
  const Donate = async () => {
    console.log("backend url is ")
    // if(user === null) {
    //   return setShowModal(true);
    // }
    const callbacks = {
      onReadyForServerApproval,
      onReadyForServerCompletion,
      onCancel,
      onError
    };
    const payment = await window.Pi.createPayment(
      {
                    // Amount of π to be paid:
                    amount: 5.00,
                    // An explanation of the payment
                    memo: "Donation",
                    // An arbitrary developer-provided metadata object
                    metadata: { paymentType: "Donation Test" },
                }, callbacks);
    console.log(payment);
  }







  //end of my additions

  const onIncompletePaymentFound = (payment: PaymentDTO) => {
    console.log("onIncompletePaymentFound", payment);
    return axiosClient.post('/payments/incomplete', {payment});
  }

  const onReadyForServerApproval = (paymentId: string) => {
    console.log("onReadyForServerApproval", paymentId);
    axiosClient.post('/payments/approve', {paymentId}, config);
  }

  const onReadyForServerCompletion = (paymentId: string, txid: string) => {
    console.log("onReadyForServerCompletion", paymentId, txid);
    axiosClient.post('/payments/complete', {paymentId, txid}, config);
  }

  const onCancel = (paymentId: string) => {
    console.log("onCancel", paymentId);
    return axiosClient.post('/payments/cancelled_payment', {paymentId});
  }

  const onError = (error: Error, payment?: PaymentDTO) => {
    console.log("onError", error);
    if (payment) {
      console.log(payment);
      // handle the error accordingly
    }
  }


















// // Authenticate the user, and get permission to request payments from them:
// const scopes = ['payments'];

// // Read more about this callback in the SDK reference:
// function onIncompletePaymentFound(payment) { /* ... */ };

// Pi.authenticate(scopes, onIncompletePaymentFound).then(function(auth) {
//   console.log(`Hi there! You're ready to make payments!`);
// }).catch(function(error) {
//   console.error(error);
// });


// Pi.createPayment({
//   // Amount of π to be paid:
//   amount: 3.14,
//   // An explanation of the payment - will be shown to the user:
//   memo: "...", // e.g: "Digital kitten #1234",
//   // An arbitrary developer-provided metadata object - for your own usage:
//   metadata: { /* ... */ }, // e.g: { kittenId: 1234 }
// }, {
//   // Callbacks you need to implement - read more about those in the detailed docs linked below:
//   onReadyForServerApproval: function(paymentId) { /* ... */ },
//   onReadyForServerCompletion: function(paymentId, txid) { /* ... */ },
//   onCancel: function(paymentId) { /* ... */ },
//   onError: function(error, payment) { /* ... */ },
// });