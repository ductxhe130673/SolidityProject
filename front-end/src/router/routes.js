import Index from "../views/Index.vue";
import Login from "../views/Login.vue"
import Register from "../views/Register.vue"
import SelectSc from "../views/SelectSc.vue"
import SelectContext from "../views/SelectContext.vue"
import InitialMarkingSetting from "../views/InitialMarkingSetting.vue"
import ChooseProperty from "../views/ChooseProperty"

import ListOfCheckedTransactions from "../views/select-sc/transactions/ListOfCheckedTransactions.vue"
import CheckReenTrancyDetail from "../views/select-sc/transactions/CheckReenTrancyDetail.vue"
import CheckingResult from "../views/select-sc/transactions/CheckingResult.vue"

import SelectSmartContract from "../views/select-sc/smartcontract/SelectSmartContract.vue"
import UpLoadSc from "../views/select-sc/smartcontract/UpLoadSc.vue"

import ContextOfSmartContract from "../views/context/ContextOfSmartContract.vue"
import LoadContext from "../views/context/LoadContext.vue"
import UpLoadContext from "../views/context/UpLoadContext.vue"

import LTLCheckingOption from "../views/choose-property/LTLCheckingOption.vue"
import ContractSpecificProperty from "../views/choose-property/CheckContractSpecificProperty/ContractSpecificProperty.vue"
import CSPTemplateSetting from "../views/choose-property/CheckContractSpecificProperty/CSPTemplate/CSPTemplateSetting.vue"
import CheckingSmartContract from "../views/CheckingSmartContract.vue"
import checkingresult31 from "../views/checkingresult31.vue"

import ContractSpecificPropertyNonTemplate from "../views/choose-property/CheckContractSpecificProperty/ContractSpecificPropertyNonTemplate.vue"

import ChooseEleOfSC from "../views/choose-property/CheckGeneralVul/ChooseElementOfTheSmartContract.vue"
import GenaralVulSetting from "../views/choose-property/CheckGeneralVul/GenaralVulSetting.vue"
import VulnerabilitySummary from "../views/choose-property/CheckGeneralVul/VulnerabilitySummary.vue"
import SelectFuncTimeStampSkipEmpty from "../views/choose-property/select-op/SelectFuncTimeStampSkipEmpty.vue"

import ListContext from "../views/context/context-crud/list-context.vue"
import AddContext from "../views/context/context-crud/add-context.vue"
import EditContext from "../views/context/context-crud/edit-context.vue"

import ListSc from "../views/select-sc/smartcontract-crud/list-sc.vue"
import EditSc from "../views/select-sc/smartcontract-crud/edit-sc.vue"
import AddSc from "../views/select-sc/smartcontract-crud/add-sc.vue"
import SelectSContractSD2 from "../views/select-sc/select/SelectSContractSD2.vue"
import SelectFuncSD from "../views/select-sc/select/SelectFuncSD.vue"

import AddVul from "../views/vuls-crud/add-vul.vue"
import EditVul from "../views/vuls-crud/edit-vul.vue"
import ListVul from "../views/vuls-crud/list-vulnerabilities.vue"

import SelectFunction from "../views/add-sagemented/SelectFunction.vue"
import SelectGlobalVariable from "../views/add-sagemented/SelectGlobalVariable.vue"
import SelectLocalVariable from "../views/add-sagemented/SelectLocalVariable.vue"
import SelectContract from "../views/add-sagemented/SelectSmartContract.vue"
import RoadMap from "../views/RoadMap.vue"

import { DOMAIN_TITLE } from '../.env'




import InitialMarkingLink from "../views/InitialMarkingLink.vue"
import SelectVarReentrancyOp1 from "../views/choose-property/select-op/SelectVarReentrancyOp1.vue"
import SelectFuncReentrancyOp1 from "../views/choose-property/select-op/SelectFuncReentrancyOp1.vue"
import SelectFuncReentrancyOp2 from "../views/choose-property/select-op/SelectFuncReentrancyOp2.vue"
import SelectSCRentrancyOp2 from "../views/choose-property/select-op/SelectSCRentrancyOp2.vue"
import SelectVarReentrancyOp2 from "../views/choose-property/select-op/SelectVarReentrancyOp2.vue"

export const routes = [{
        path: "/",
        name: "Index",
        component: Index,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | home` },
    },
    {
        path: "/roadmap",
        name: "RoadMap",
        component: RoadMap,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | RoadMap` },
        props: true
      },
    {
        path: "/login",
        name: "Login",
        component: Login,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | login` },
    },
    {
        path: "/register",
        name: "Register",
        component: Register,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | register` },
    },
    {
        path: "/select-sc/",
        name: "SelectSc",
        component: SelectSc,
        children: [{
                path: 'listofcheckedtransactions',
                name: 'ListOfCheckedTransactions',
                component: ListOfCheckedTransactions,
                meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | listofcheckedtransactions` },
            },
            {
                path: 'checkreentrancydetail',
                name: 'CheckRentrancy',
                component: CheckReenTrancyDetail,
                meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | checkreentrancydetail` }
            },
            {
                path: 'checking-result',
                name: 'CheckingResult',
                component: CheckingResult
            },
            {
                path: 'select-smart-contract',
                name: 'SelectSmartContract',
                component: SelectSmartContract
            },
            {
                path: 'uploadsc',
                name: 'UpLoadSc',
                component: UpLoadSc
            },
            {
                path: 'selectscsd2',
                name: 'SelectSContractSD2',
                component: SelectSContractSD2
            },
            {
                path: 'SelectFuncSD',
                name: 'SelectFuncSD',
                component: SelectFuncSD
            }

        ],
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | checkreentrancydetail` },
    },
    {
        path: "/context/",
        name: "SelectContext",
        component: SelectContext,
        children: [{
                path: 'context-of-smartcontract',
                name: 'ContextOfSmartContract',
                component: ContextOfSmartContract
            },
            {
                path: 'load-context',
                name: 'LoadContext',
                component: LoadContext
            },
            {
                path: 'uploadcontext',
                name: 'UpLoadContext',
                component: UpLoadContext
            }
        ],
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | select context` },
    },
    {
        path: "/choose-property/",
        name: "ChooseProperty",
        component: ChooseProperty,
        children: [{
                path: "ltlcheck-option",
                name: "LTLCheckOption",
                component: LTLCheckingOption,
            },
            {
                path: "csp-template-setting",
                name: "CSPTemplateSetting",
                component: CSPTemplateSetting
            },
            {
                path: "csp-setting-types",
                name: "CSPSettingType",
                component: ContractSpecificProperty
            },
            {
                path: "csp-non-template-setting",
                name: "CSPNonTemplateSetting",
                component: ContractSpecificPropertyNonTemplate
            },
            {
                path: "genaral-vul-setting",
                name: "GenaralVulSetting",
                component: GenaralVulSetting
            },
            {
                path: "choose-ele-contract",
                name: "ChooseElementOfSmartContract",
                component: ChooseEleOfSC
            },
            {
                path: "vul-summary",
                name: "VulSummary",
                component: VulnerabilitySummary
            },
            {
                path: "select-function",
                name: "SelectFuntion",
                component: SelectFunction
            },
            {
                path: "select-global-variable",
                name: "SelectGlobalVariable",
                component: SelectGlobalVariable
            },
            {
                path: "select-local-variable",
                name: "SelectLocalVariable",
                component: SelectLocalVariable
            },
            {
                path: "select-smart-contract",
                name: "SelectContract",
                component: SelectContract
            },
            {
                path: "SelectFTSSkip",
                name: "SelectFuncTimeStampSkipEmpty",
                component: SelectFuncTimeStampSkipEmpty
            },

        ],
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | choose property` },
    },
    {
        path: "/initialmarking",
        name: "Initial",
        component: InitialMarkingSetting,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Initial` },
    },
    {
        path: "/check-sc",
        name: "CheckSmartContract",
        component: CheckingSmartContract,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Initial` },
    },
    {
        path: "/InitialMarkingLink",
        name: "InitialMarkingLink",
        component: InitialMarkingLink,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Initial Marking Link` },
    },
    {
        path: "/check-rs",
        name: "checkingresult31",
        component: checkingresult31,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Initial` },
    },
    {
        path: "/list-context",
        name: "ListContext",
        component: ListContext,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | List Of Contexts` },
        props: true
    },
    {
        path: "/list-sc",
        name: "ListSc",
        component: ListSc,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | list smart contracts` },
    },
    {
        path: "/edit-sc",
        name: "EditSc",
        component: EditSc,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | edit smart contracts` },
        props: true
    },

    {
        path: "/add-sc",
        name: "AddSc",
        component: AddSc,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | create smart contracts` },
        props: true
    },
    {
        path: "/add-context",
        name: "AddContext",
        component: AddContext,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Add a Context` },
        props: true
    },
    {
        path: "/edit-context",
        name: "EditContext",
        component: EditContext,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Edit Context` },
        props: true
    },
    {
        path: "/list-vul",
        name: "ListVul",
        component: ListVul,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | List Of Vulnerabilities` },
        props: true
    },
    {
        path: "/add-vul",
        name: "AddVul",
        component: AddVul,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Add an LTL Vulnerability` },
        props: true
    },
    {
        path: "/edit-vul",
        name: "EditVul",
        component: EditVul,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Edit an LTL Vulnerability` },
        props: true
    },
    {
        path: "/SelectVarReentrancyOp1",
        name: "SelectVarReentrancyOp1",
        component: SelectVarReentrancyOp1,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Select Var Reentrancy Op1` },
    },
    {
        path: "/SelectFuncReentrancyOp1",
        name: "SelectFuncReentrancyOp1",
        component: SelectFuncReentrancyOp1,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Select Func Reentrancy Op1` },
    },
    {
        path: "/SelectFuncReentrancyOp2",
        name: "SelectFuncReentrancyOp2",
        component: SelectFuncReentrancyOp2,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Select Func Reentrancy Op2` },
    },
    {
        path: "/SelectSCRentrancyOp2",
        name: "SelectSCRentrancyOp2",
        component: SelectSCRentrancyOp2,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Select SC Reentrancy Op2` },
    },
    {
        path: "/SelectVarReentrancyOp2",
        nam: "SelectVarReentrancyOp2",
        component: SelectVarReentrancyOp2,
        meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Select Var Reentrancy Op2` },
    }

]

/*
{
    path: "/list-sc",
    name: "ListSc",
    component: ListSc,
    meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | list smart contracts` },
  },
  {
    path: "/edit-sc",
    name: "EditSc",
    component: EditSc,
    meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | edit smart contracts` },
    props: true
  },
  {
    path: "/add-sc",
    name: "AddSc",
    component: AddSc,
    meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | create smart contracts` },
    props: true
  },
  {
    path: "/process",
    name: "Processing",
    component: Processing,
    meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | processing` },
  },
  {
    path: "/create-csp",
    name: "CreateCsp",
    component: CreateCsp,
    meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | create contract-specific property` },
    props: true
  },
  
  {
    path: "/add-context",
    name: "AddContext",
    component: AddContext,
    meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Add a Context` },
    props: true
  },
  {
    path: "/edit-context",
    name: "EditContext",
    component: EditContext,
    meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Edit Context` },
    props: true
  },
  {
    path: "/list-context",
    name: "ListContext",
    component: ListContext,
    meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | List Of Contexts` },
    props: true
  },
  {
    path: "/list-vul",
    name: "ListVul",
    component: ListVul,
    meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | List Of Vulnerabilities` },
    props: true
  },
  {
    path: "/add-vul",
    name: "AddVul",
    component: AddVul,
    meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Add an LTL Vulnerability` },
    props: true
  },
  {
    path: "/edit-vul",
    name: "EditVul",
    component: EditVul,
    meta: { requiresAuth: true, title: `${DOMAIN_TITLE} | Edit an LTL Vulnerability` },
    props: true
  },
*/