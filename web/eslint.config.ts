import * as js from '@eslint/js';
import plugin from '@typescript-eslint/eslint-plugin';
import parser from '@typescript-eslint/parser';
import * as react from 'eslint-plugin-react';
import * as reactHooks from 'eslint-plugin-react-hooks';

export default [
  {
    files: ['**/*.ts', '**/*.tsx'],
    languageOptions: {
      parser,
      parserOptions: {
        project: './tsconfig.eslint.json',
      },
    },
    plugins: {
      '@typescript-eslint': plugin,
      react,
      'react-hooks': reactHooks,
    },
    rules: {
      ...js.configs.recommended.rules,
      ...plugin.configs.recommended.rules,
      'react/react-in-jsx-scope': 'off',
      'react-hooks/rules-of-hooks': 'error',
      'react-hooks/exhaustive-deps': 'warn',
    },
  },
];
