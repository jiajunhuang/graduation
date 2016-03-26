module.exports = {
  'root': true,
  'extends': 'standard',
  'plugins': [
    'html'
  ],
  'env': {
    'browser': true,
    'es6': true,
    'node': true
  },
  'ecmaFeatures': {
    'arrowFunctions': true,
    'destructuring': true,
    'classes': true,
    'defaultParams': true,
    'blockBindings': true,
    'modules': true,
    'objectLiteralComputedProperties': true,
    'objectLiteralShorthandMethods': true,
    'objectLiteralShorthandProperties': true,
    'restParams': true,
    'spread': true,
    'templateStrings': true
  },
  // add your custom rules here
  'rules': {
    // allow paren-less arrow functions
    'arrow-parens': 0,
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
    'arrow-parens': 0,
    'no-console': 1,
    'no-extra-boolean-cast': 1,
    'block-scoped-var': 1,
    'default-case': 1,
    'dot-notation': [2, {
      'allowKeywords': false,
      'allowPattern': '^[a-z]+(_[a-z]+)+$'
    }],
    'eqeqeq': [2, 'smart'],
    'no-extend-native': 1,
    'no-implicit-coercion': 0,
    'no-native-reassign': 1,
    'no-redeclare': [2, {
      'builtinGlobals': true
    }],
    'no-warning-comments': [1, {
      'terms': ['TODO', 'HACK', 'XXX', 'FIXME'],
      'location': 'start'
    }],
    'vars-on-top': 0,
    'wrap-iife': [2, 'any'],
    'init-declarations': 0,
    'no-unused-expressions': [2, {
      'allowShortCircuit': true,
      'allowTernary': true
    }],
    'no-unused-vars': [2, {
      'vars': 'local',
      'args': 'after-used'
    }],
    'brace-style': 2,
    'func-style': 0,
    'func-names': 0,
    'consistent-this': [2, 'that'],
    'linebreak-style': [2, 'unix'],
    'key-spacing': [2, {
      'beforeColon': false,
      'afterColon': true
    }],
    'indent': [2, 2, {
      'SwitchCase': 2
    }],
    'lines-around-comment': [2, {
      'beforeBlockComment': true,
      'afterBlockComment': true
    }],
    'new-parens': 2,
    'no-inline-comments': 2,
    'no-lonely-if': 2,
    'no-mixed-spaces-and-tabs': 2,
    'no-multiple-empty-lines': [2, {
      'max': 3,
      'maxEOF': 1
    }],
    'no-negated-condition': 2,
    'no-nested-ternary': 1,
    'no-trailing-spaces': [2, {
      'skipBlankLines': true
    }],
    'no-ternary': 0,
    'no-restricted-syntax': [2, 'WithStatement'],
    'object-curly-spacing': [2, 'always', {
      'objectsInObjects': false,
      'arraysInObjects': false
    }],
    'one-var': [2, 'never'],
    'operator-assignment': [2, 'never'],
    'operator-linebreak': [2, 'before'],
    'quotes': [2, 'single', 'avoid-escape'],
    'quote-props': [2, 'as-needed'],
    'semi': [2, 'never'],
    'sort-vars': 0,
    'keyword-spacing': 2,
    'space-before-blocks': 2,
    'space-before-function-paren': [2, {
      'anonymous': 'always',
      'named': 'never'
    }],
    'max-len': [2, 120, 4],
    'max-params': [1, 4],
    'max-statements': [2, 50],
    'no-plusplus': [2,{
      'allowForLoopAfterthoughts': true
    }],
    'comma-dangle': [2, 'never'],
    'no-sequences': 2,
    'guard-for-in': 2,
    'no-sparse-arrays': 2,
    'no-new': 0
  }
}
