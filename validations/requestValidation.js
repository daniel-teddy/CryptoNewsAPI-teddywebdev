const Yup = require("yup");

exports.requestSchema = Yup.object().shape({
  refMerchantStore: Yup.number().required(),
  phone: Yup.string().required(),
  amount: Yup.number().required(),
  pack: Yup.string().required(),
  lang: Yup.string().oneOf(["tr"]).required(),
  currency: Yup.string().oneOf(["TRY"]).required(),
  message: Yup.string().required(),
  date: Yup.string().required(),
});
